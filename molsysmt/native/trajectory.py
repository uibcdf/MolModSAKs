import numpy as np
from molsysmt import puw
from molsysmt._private_tools.exceptions import *

# Tiene que haber una manera automatica con f2py dar siempre de salida Ccontiguous_np.arrays

# Un frame tiene: step, time, coordinates, cell

class Trajectory():

    def __init__(self, filepath=None, atom_indices='all', frame_indices='all'):

        self.step  = None
        self.time  = None
        self.coordinates = None # ndarray with shape=(n_frames, n_atoms, 3) and dtype=float
                                # and order=F, with units nanometers
        self.box  = None # ndarray with shape=(n_frames,3,3), dtype=float and order='F'
                          # cell is the matrix with the vectors
        self.n_frames = 0
        self.n_atoms = 0

        self.file = None

        if filepath is not None:
            self.load_frames_from_file(filepath=filepath, atom_indices=atom_indices, frame_indices=frame_indices)

    def append_frames(self, step=None, time=None, coordinates=None, box=None):

        if step is not None:
            if type(step) not in [list, np.ndarray]:
                step  = np.array([step])
            else:
                step = step

        if time is not None:
            time=puw.standardize(time)
        if coordinates is not None:
            coordinates=puw.standardize(coordinates)
        if box is not None:
            box=puw.standardize(box)

        n_frames = coordinates.shape[0]
        n_atoms = coordinates.shape[1]

        if self.n_frames == 0:

            self.coordinates = coordinates
            self.step = step
            self.time = time
            self.box = box
            self.n_frames = n_frames
            self.n_atoms = n_atoms

        else:

            if n_atoms!=self.n_atoms:
                raise ValueError("The coordinates to be appended in the system needs to have the same number of atoms.")

            if step is not None:
                if self.step is None:
                    raise ValueError("The trajectory has no steps to append the new frame.")
                else:
                    self.step = np.concatenate([self.step, step])

            if time is not None:
                if self.time is None:
                    raise ValueError("The trajectory has no time array to append the new frame.")
                else:
                    self.time = np.concatenate([self.time, time])

            if box is not None:
                if self.box is None:
                    raise ValueError("The trajectory has no box array to append the new frame.")
                else:
                    self.box = np.concatenate([self.box, box])

            self.coordinates = np.concatenate([self.coordinates, coordinates])

            self.n_frames += n_frames

        pass

    def get_box_lengths(self):

        from molsysmt.pbc import box_lengths_from_box_vectors

        if self.box is not None:
            lengths = box_lengths_from_box_vectors(self.box)
        else:
            lengths = None

        return lengths

    def get_box_angles(self):

        from molsysmt.pbc import box_angles_from_box_vectors

        if self.box is not None:
            angles = box_angles_from_box_vectors(self.box)
        else:
            angles = None

        return angles

    def load_frames_from_file (self, filepath=None, atom_indices='all', frame_indices='all'):

        if filepath is not None:

            from .trajectory_file import TrajectoryFile
            self.file = TrajectoryFile(filepath=filepath)

        step, time, coordinates, box = self.file.read_frames(atom_indices=atom_indices, frame_indices=frame_indices)

        self.append_frames(step, time, coordinates, box)

        del(coordinates, time, step, box)

        pass

    def extract (self, atom_indices='all', frame_indices='all'):

        if atom_indices is 'all' and frame_indices is 'all':

            tmp_item = self.copy()

        else:

            from copy import deepcopy

            tmp_item = Trajectory()

            if self.step is not None:
                if frame_indices is not 'all':
                    tmp_item.step = self.step[frame_indices]
                else:
                    tmp_item.step = deepcopy(self.step)

            if self.time is not None:
                if frame_indices is not 'all':
                    tmp_item.time = self.time[frame_indices]
                else:
                    tmp_item.time = deepcopy(self.time)

            if self.box is not None:
                if frame_indices is not 'all':
                    tmp_item.box = self.box[frame_indices]
                else:
                    tmp_item.box = deepcopy(self.box)

            if atom_indices is not 'all':
                tmp_item.coordinates = self.coordinates[:,atom_indices,:]
            else:
                tmp_item.coordinates = deepcopy(self.coordinates)

            if frame_indices is not 'all':
                tmp_item.coordinates = tmp_item.coordinates[frame_indices,:,:]

            tmp_item.n_frames = tmp_item.coordinates.shape[0]
            tmp_item.n_atoms = tmp_item.coordinates.shape[1]

            if self.file is not None:
                tmp_item.file = self.file.copy()

        return tmp_item

    def add(self, item, selection='all', frame_indices='all'):

        from molsysmt.multitool import get

        step, time, coordinates, box = get(item, target="atom", selection=selection, frame_indices=frame_indices, frame=True)

        if self.n_frames==0:
            self.append_frames(step, time, coordinates, box)
        else:
            if self.n_frames != coordinates.shape[0]:
                raise ValueError('Both items need to have the same n_frames')
            else:
                unit = puw.get_unit(self.coordinates)
                value_coordinates = puw.get_value(coordinates, to_unit=unit)
                value_self_coordinates = puw.get_value(self.coordinates)
                self.coordinates = np.hstack([value_self_coordinates, value_coordinates])*unit
                del(value_coordinates, value_self_coordinates)

        self.n_atoms = self.coordinates.shape[1]

        pass

    def append(self, item, selection='all', frame_indices='all'):

        from molsysmt.multitool import get

        step, time, coordinate, box = get(item, target="atom", selection=selection, frame_indices=frame_indices, frame=True)
        self.append_frames(step, time, coordinate, box)

        pass

    def copy (self):

        from copy import deepcopy

        tmp_item = Trajectory()

        tmp_item.step = deepcopy(self.step)
        tmp_item.time = deepcopy(self.time)
        tmp_item.coordinates = deepcopy(self.coordinates)
        tmp_item.box = deepcopy(self.box)

        tmp_item.n_frames = deepcopy(self.n_frames)
        tmp_item.n_atoms = deepcopy(self.n_atoms)

        if self.file is not None:
            tmp_item.file = self.file.copy()
        else:
            tmp_item.file = None

        return tmp_item


    #def cell2box(self):
    #    self.box,self.volume,self.orthogonal=_libbox.cell2box(self.cell, self.n_frames)
    #    pass

    #def box2cell(self):
    #    self.cell,self.volume,self.orthogonal=_libbox.box2cell(self.box, self.n_frames)
    #    pass

    #def box2invbox(self):
    #    self.invbox=_libbox.box2invbox(self.box, self.n_frames)
    #    pass

    #def iterload(self, chunk=100, stride=1, skip=0, atom_indices=None):

    #    atom_indices = None

    #    if selection is None:
    #        if self.selection_mdtraj is not None:
    #            atom_indices = self._atom_indices_mdtraj
    #    else:
    #        from molsysmt.multitool import select as _select
    #        atom_indices = _select(self.topology_mdtraj,selection,syntaxis)

    #    from mdtraj import iterload as _mdtraj_iterload
    #    tmp_top = self.topology_mdtraj

    #    iterator = _mdtraj_iterload(self.filename, top=tmp_top, chunk=chunk,
    #                                            stride=stride, atom_indices=atom_indices)

    #    while True:
    #        try:
    #            tmp_mdtraj = next(iterator)
    #        except StopIteration:
    #            return
    #        self._import_mdtraj_data(tmp_mdtraj)
    #        if atom_indices is not None:
    #            self._import_mdtraj_topology(tmp_mdtraj)
    #        del(tmp_mdtraj)
    #        yield


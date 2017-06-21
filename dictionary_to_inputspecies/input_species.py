
species(
    label='H(3)',
    reactive=True,
    structure=adjacencyList(
        """
        1 H u1 p0 c0
        """),
)
            
species(
    label='O(4)',
    reactive=True,
    structure=adjacencyList(
        """
        1 O u2 p2 c0
        """),
)
            
species(
    label='OH(5)',
    reactive=True,
    structure=adjacencyList(
        """
        1 O u1 p2 c0 {2,S}
        2 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='H2(6)',
    reactive=True,
    structure=adjacencyList(
        """
        1 H u0 p0 c0 {2,S}
        2 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='H2O(7)',
    reactive=True,
    structure=adjacencyList(
        """
        1 O u0 p2 c0 {2,S} {3,S}
        2 H u0 p0 c0 {1,S}
        3 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='HO2(8)',
    reactive=True,
    structure=adjacencyList(
        """
        1 O u0 p2 c0 {2,S} {3,S}
        2 O u1 p2 c0 {1,S}
        3 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='H2O2(9)',
    reactive=True,
    structure=adjacencyList(
        """
        1 O u0 p2 c0 {2,S} {3,S}
        2 O u0 p2 c0 {1,S} {4,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='CO(10)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p1 c-1 {2,T}
        2 O u0 p1 c+1 {1,T}
        """),
)
            
species(
    label='CO2(11)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,D} {3,D}
        2 O u0 p2 c0 {1,D}
        3 O u0 p2 c0 {1,D}
        """),
)
            
species(
    label='HOCO(12)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u1 p0 c0 {2,S} {3,D}
        2 O u0 p2 c0 {1,S} {4,S}
        3 O u0 p2 c0 {1,D}
        4 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='CH2O(13)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,D} {3,S} {4,S}
        2 O u0 p2 c0 {1,D}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='HCO(14)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u1 p0 c0 {2,D} {3,S}
        2 O u0 p2 c0 {1,D}
        3 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='CH3(15)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u1 p0 c0 {2,S} {3,S} {4,S}
        2 H u0 p0 c0 {1,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='CH4(16)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 H u0 p0 c0 {1,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='CH2(17)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u2 p0 c0 {2,S} {3,S}
        2 H u0 p0 c0 {1,S}
        3 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='CH2(S)(18)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p1 c0 {2,S} {3,S}
        2 H u0 p0 c0 {1,S}
        3 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='CH3O(19)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 O u1 p2 c0 {1,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='C2H5(20)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u1 p0 c0 {1,S} {6,S} {7,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='CH3OH(21)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 O u0 p2 c0 {1,S} {6,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='CH2OH(22)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u1 p0 c0 {2,S} {3,S} {4,S}
        2 O u0 p2 c0 {1,S} {5,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='CH3OOH(23)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2 O u0 p2 c0 {1,S} {3,S}
        3 O u0 p2 c0 {2,S} {7,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='CH3OO(24)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 O u0 p2 c0 {1,S} {6,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 O u1 p2 c0 {2,S}
        """),
)
            
species(
    label='C2H5O(25)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
        3 O u1 p2 c0 {2,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='C2H6(26)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='CH3CHO(27)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {6,D} {7,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 O u0 p2 c0 {2,D}
        7 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='C2H4(28)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,D} {3,S} {4,S}
        2 C u0 p0 c0 {1,D} {5,S} {6,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {2,S}
        6 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='C2H3(29)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,D} {3,S} {4,S}
        2 C u1 p0 c0 {1,D} {5,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='CH2CHO(30)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u1 p0 c0 {2,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {3,D} {6,S}
        3 O u0 p2 c0 {2,D}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='cC2H4O(31)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
        3 O u0 p2 c0 {1,S} {2,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='C2H2(32)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,T} {3,S}
        2 C u0 p0 c0 {1,T} {4,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='CH2CO(33)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,D} {3,S} {4,S}
        2 C u0 p0 c0 {1,D} {5,D}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 O u0 p2 c0 {2,D}
        """),
)
            
species(
    label='C2H3O2(34)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,D} {3,S} {4,S}
        2 C u0 p0 c0 {1,D} {5,S} {6,S}
        3 O u0 p2 c0 {1,S} {7,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {2,S}
        6 H u0 p0 c0 {2,S}
        7 O u1 p2 c0 {3,S}
        """),
)
            
species(
    label='C2H(35)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,T} {3,S}
        2 C u1 p0 c0 {1,T}
        3 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='HCCO(36)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u1 p0 c0 {2,D} {4,S}
        2 C u0 p0 c0 {1,D} {3,D}
        3 O u0 p2 c0 {2,D}
        4 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='H2CC(37)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,D} {3,S} {4,S}
        2 C u0 p1 c0 {1,D}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='C2(38)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u1 p0 c0 {2,T}
        2 C u1 p0 c0 {1,T}
        """),
)
            
species(
    label='C2O(39)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,D} {3,D}
        2 C u2 p0 c0 {1,D}
        3 O u0 p2 c0 {1,D}
        """),
)
            
species(
    label='C2H6O(40)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
        3 O u0 p2 c0 {1,S} {9,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {2,S}
        9 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C2H5O(41)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2 C u1 p0 c0 {1,S} {3,S} {7,S}
        3 O u0 p2 c0 {2,S} {8,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C2H5O(42)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u1 p0 c0 {1,S} {6,S} {7,S}
        3 O u0 p2 c0 {1,S} {8,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C2H4O(43)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,D} {3,S} {4,S}
        2 C u0 p0 c0 {1,D} {5,S} {6,S}
        3 O u0 p2 c0 {1,S} {7,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {2,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='CH3CO(44)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u1 p0 c0 {1,S} {6,D}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 O u0 p2 c0 {2,D}
        """),
)
            
species(
    label='cC2H3O(45)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u1 p0 c0 {1,S} {3,S} {6,S}
        3 O u0 p2 c0 {1,S} {2,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='CHCHOH(46)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,D} {3,S} {4,S}
        2 C u1 p0 c0 {1,D} {5,S}
        3 O u0 p2 c0 {1,S} {6,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {2,S}
        6 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='OCHCHO(47)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,D} {5,S}
        2 C u0 p0 c0 {1,S} {4,D} {6,S}
        3 O u0 p2 c0 {1,D}
        4 O u0 p2 c0 {2,D}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='HCCOH(48)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,T} {3,S}
        2 C u0 p0 c0 {1,T} {4,S}
        3 O u0 p2 c0 {1,S} {5,S}
        4 H u0 p0 c0 {2,S}
        5 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C2H6O2(49)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  O u0 p2 c0 {1,S} {4,S}
        4  O u0 p2 c0 {3,S} {10,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='C2H5O2(50)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
        3 O u0 p2 c0 {1,S} {9,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {2,S}
        9 O u1 p2 c0 {3,S}
        """),
)
            
species(
    label='C2H5O2(51)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2 C u1 p0 c0 {1,S} {7,S} {8,S}
        3 O u0 p2 c0 {1,S} {4,S}
        4 O u0 p2 c0 {3,S} {9,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {2,S}
        9 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='C2H4O2(52)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,D} {3,S} {5,S}
        2 C u0 p0 c0 {1,D} {6,S} {7,S}
        3 O u0 p2 c0 {1,S} {4,S}
        4 O u0 p2 c0 {3,S} {8,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='C3H6O(53)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {9,D} {10,S}
        4  H u0 p0 c0 {1,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  O u0 p2 c0 {3,D}
        10 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C2H5CO(54)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
        3 C u1 p0 c0 {1,S} {9,D}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {2,S}
        9 O u0 p2 c0 {3,D}
        """),
)
            
species(
    label='C3H6(55)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2 C u0 p0 c0 {1,S} {3,D} {7,S}
        3 C u0 p0 c0 {2,D} {8,S} {9,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {3,S}
        9 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C3H4(56)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {3,D} {4,S} {5,S}
        2 C u0 p0 c0 {3,D} {6,S} {7,S}
        3 C u0 p0 c0 {1,D} {2,D}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='C3H5(57)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,D} {4,S}
        2 C u1 p0 c0 {1,S} {5,S} {6,S}
        3 C u0 p0 c0 {1,D} {7,S} {8,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {2,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {3,S}
        8 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C3H5(58)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
        2 C u0 p0 c0 {3,D} {7,S} {8,S}
        3 C u1 p0 c0 {1,S} {2,D}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='C3H5(59)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2 C u0 p0 c0 {1,S} {3,D} {7,S}
        3 C u1 p0 c0 {2,D} {8,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C3H4O(60)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2 C u0 p0 c0 {1,S} {3,D} {7,S}
        3 C u0 p0 c0 {2,D} {8,D}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 H u0 p0 c0 {2,S}
        8 O u0 p2 c0 {3,D}
        """),
)
            
species(
    label='H3CCCH(61)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2 C u0 p0 c0 {1,S} {3,T}
        3 C u0 p0 c0 {2,T} {7,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C3H4O(62)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,D} {3,S} {4,S}
        2 C u0 p0 c0 {1,D} {6,S} {7,S}
        3 C u0 p0 c0 {1,S} {5,D} {8,S}
        4 H u0 p0 c0 {1,S}
        5 O u0 p2 c0 {3,D}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='H2CCCH(63)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u1 p0 c0 {2,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {3,T}
        3 C u0 p0 c0 {2,T} {6,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C3H2(64)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,D} {3,D}
        2 C u1 p0 c0 {1,D} {4,S}
        3 C u1 p0 c0 {1,D} {5,S}
        4 H u0 p0 c0 {2,S}
        5 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='He',
    reactive=True,
    structure=adjacencyList(
        """
        1 He u0 p1 c0
        """),
)
            
species(
    label='Ar',
    reactive=True,
    structure=adjacencyList(
        """
        1 Ar u0 p4 c0
        """),
)
            
species(
    label='Ne',
    reactive=True,
    structure=adjacencyList(
        """
        1 Ne u0 p4 c0
        """),
)
            
species(
    label='N2',
    reactive=True,
    structure=adjacencyList(
        """
        1 N u0 p1 c0 {2,T}
        2 N u0 p1 c0 {1,T}
        """),
)
            
species(
    label='nC7H16(1)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
        2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
        3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
        4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
        5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
        6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
        7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
        8  H u0 p0 c0 {4,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {5,S}
        18 H u0 p0 c0 {6,S}
        19 H u0 p0 c0 {6,S}
        20 H u0 p0 c0 {6,S}
        21 H u0 p0 c0 {7,S}
        22 H u0 p0 c0 {7,S}
        23 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='O2(2)',
    reactive=True,
    structure=adjacencyList(
        """
        1 O u1 p2 c0 {2,S}
        2 O u1 p2 c0 {1,S}
        """),
)
            
species(
    label='C7H15(138)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
        2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
        3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
        5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
        6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
        7  C u1 p0 c0 {4,S} {6,S} {22,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {5,S}
        18 H u0 p0 c0 {5,S}
        19 H u0 p0 c0 {6,S}
        20 H u0 p0 c0 {6,S}
        21 H u0 p0 c0 {6,S}
        22 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='C4H9(132)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        4  C u1 p0 c0 {2,S} {12,S} {13,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='C7H15(135)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
        2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
        4  C u0 p0 c0 {6,S} {7,S} {14,S} {15,S}
        5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
        6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
        7  C u1 p0 c0 {3,S} {4,S} {22,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {5,S}
        18 H u0 p0 c0 {5,S}
        19 H u0 p0 c0 {6,S}
        20 H u0 p0 c0 {6,S}
        21 H u0 p0 c0 {6,S}
        22 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='C3H7(133)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
        3  C u1 p0 c0 {1,S} {9,S} {10,S}
        4  H u0 p0 c0 {1,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C5H11(134)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
        4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
        5  C u1 p0 c0 {3,S} {15,S} {16,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(3951)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
        4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
        5  C u0 p0 c0 {3,S} {4,S} {14,S} {15,S}
        6  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(4354)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
        3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
        5  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
        6  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
        7  C u0 p0 c0 {4,S} {21,S} {22,S} {23,S}
        8  O u0 p2 c0 {1,S} {24,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {5,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {2,S}
        15 H u0 p0 c0 {2,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {6,S}
        19 H u0 p0 c0 {6,S}
        20 H u0 p0 c0 {6,S}
        21 H u0 p0 c0 {7,S}
        22 H u0 p0 c0 {7,S}
        23 H u0 p0 c0 {7,S}
        24 O u1 p2 c0 {8,S}
        """),
)
            
species(
    label='S(4324)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
        5  C u0 p0 c0 {2,S} {6,D} {18,S}
        6  C u0 p0 c0 {4,S} {5,D} {17,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(4163)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
        3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
        4  C u0 p0 c0 {2,S} {3,S} {14,S} {15,S}
        5  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
        6  C u0 p0 c0 {1,S} {21,S} {22,S} {23,S}
        7  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
        8  O u0 p2 c0 {1,S} {24,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {5,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {2,S}
        17 H u0 p0 c0 {2,S}
        18 H u0 p0 c0 {7,S}
        19 H u0 p0 c0 {7,S}
        20 H u0 p0 c0 {7,S}
        21 H u0 p0 c0 {6,S}
        22 H u0 p0 c0 {6,S}
        23 H u0 p0 c0 {6,S}
        24 O u1 p2 c0 {8,S}
        """),
)
            
species(
    label='S(4322)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
        5  C u0 p0 c0 {2,S} {4,S} {6,D}
        6  C u0 p0 c0 {5,D} {17,S} {18,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(5232)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
        5  C u0 p0 c0 {1,S} {10,S} {17,S} {18,S}
        6  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {5,S}
        11 H u0 p0 c0 {6,S}
        12 H u0 p0 c0 {6,S}
        13 H u0 p0 c0 {6,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {5,S}
        18 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(4030)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {3,S} {6,D} {16,S}
        6  C u0 p0 c0 {5,D} {17,S} {18,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(4362)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {2,S} {6,D} {16,S}
        6  C u0 p0 c0 {5,D} {17,S} {18,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(5514)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {13,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
        5  C u0 p0 c0 {1,S} {4,S} {6,D}
        6  C u0 p0 c0 {5,D} {17,S} {18,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(5233)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        5  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
        6  C u0 p0 c0 {1,S} {13,S} {17,S} {18,S}
        7  H u0 p0 c0 {4,S}
        8  H u0 p0 c0 {4,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {6,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(3623)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        4  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(3622)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
        2  C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(4361)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {6,D} {16,S}
        6  C u0 p0 c0 {5,D} {17,S} {18,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(6640)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
        4  C u0 p0 c0 {5,S} {12,S} {16,S} {17,S}
        5  C u0 p0 c0 {3,S} {4,S} {6,D}
        6  C u0 p0 c0 {1,S} {5,D} {18,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(4819)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
        2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {6,S} {9,S} {12,S}
        5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
        6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(7011)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
        5  C u0 p0 c0 {1,S} {6,D} {18,S}
        6  C u0 p0 c0 {4,S} {5,D} {17,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(4169)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
        5  C u0 p0 c0 {2,S} {3,S} {14,S} {15,S}
        6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {4,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(5524)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
        5  C u0 p0 c0 {3,S} {6,S} {13,S} {16,S}
        6  C u0 p0 c0 {4,S} {5,S} {17,S} {18,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(5515)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {10,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {9,S} {14,S} {15,S}
        5  C u0 p0 c0 {1,S} {6,D} {16,S}
        6  C u0 p0 c0 {5,D} {17,S} {18,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(8002)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
        2  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
        3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
        5  C u0 p0 c0 {1,S} {6,D} {17,S}
        6  C u0 p0 c0 {2,S} {5,D} {18,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {5,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(6646)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
        4  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
        5  C u0 p0 c0 {1,S} {3,S} {6,D}
        6  C u0 p0 c0 {4,S} {5,D} {18,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(8841)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {6,S} {9,S} {12,S}
        5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(8001)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
        2  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
        5  C u0 p0 c0 {1,S} {2,S} {6,D}
        6  C u0 p0 c0 {5,D} {17,S} {18,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(7112)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {5,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {6,S} {9,S}
        4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
        5  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
        6  C u0 p0 c0 {3,S} {10,S} {17,S} {18,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {6,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(8836)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
        4  C u0 p0 c0 {1,S} {5,S} {12,S} {15,S}
        5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
        6  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {5,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(7419)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
        2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
        5  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
        6  C u0 p0 c0 {2,S} {13,S} {17,S} {18,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {6,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='C7H15(139)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
        2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
        3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
        4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
        5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
        6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
        7  C u1 p0 c0 {5,S} {21,S} {22,S}
        8  H u0 p0 c0 {4,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {5,S}
        18 H u0 p0 c0 {6,S}
        19 H u0 p0 c0 {6,S}
        20 H u0 p0 c0 {6,S}
        21 H u0 p0 c0 {7,S}
        22 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(4827)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
        2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
        3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
        4  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
        5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {4,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(3437)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
        3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
        4  C u0 p0 c0 {1,S} {5,D} {16,S}
        5  C u0 p0 c0 {3,S} {4,D} {15,S}
        6  O u0 p2 c0 {2,S} {7,S}
        7  O u0 p2 c0 {6,S} {17,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(3474)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
        4  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
        5  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
        6  O u0 p2 c0 {2,S} {7,S}
        7  O u0 p2 c0 {6,S} {17,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(11204)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,S} {10,S}
        3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {5,D} {14,S}
        5  C u0 p0 c0 {4,D} {15,S} {16,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {6,S} {17,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(11202)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
        4  C u0 p0 c0 {1,S} {5,D} {6,S}
        5  C u0 p0 c0 {3,S} {4,D} {16,S}
        6  O u0 p2 c0 {4,S} {7,S}
        7  O u0 p2 c0 {6,S} {17,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(1194)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {5,S} {15,D}
        5  C u1 p0 c0 {3,S} {4,S} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='C4H8(993)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,D} {10,S}
        4  C u0 p0 c0 {3,D} {11,S} {12,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(12909)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {2,S} {16,D}
        6  O u0 p2 c0 {1,S} {17,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 O u0 p2 c0 {5,D}
        17 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='C4H8(1066)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(13294)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,S} {10,D}
        4  O u0 p2 c0 {1,S} {5,S}
        5  O u0 p2 c0 {3,S} {4,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 O u0 p2 c0 {3,D}
        """),
)
            
species(
    label='C4H8(1561)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        4  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(403)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,D} {4,S} {6,S}
        2  C u0 p0 c0 {1,D} {7,S} {8,S}
        3  C u0 p0 c0 {5,S} {9,D} {10,S}
        4  O u0 p2 c0 {1,S} {5,S}
        5  O u0 p2 c0 {3,S} {4,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  O u0 p2 c0 {3,D}
        10 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='S(14859)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,S} {10,D}
        4  O u0 p2 c0 {2,S} {5,S}
        5  O u0 p2 c0 {3,S} {4,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 O u0 p2 c0 {3,D}
        """),
)
            
species(
    label='CHO2(140)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,D}
        2 H u0 p0 c0 {1,S}
        3 O u1 p2 c0 {1,S}
        4 O u0 p2 c0 {1,D}
        """),
)
            
species(
    label='S(4363)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
        4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
        5  C u0 p0 c0 {3,S} {4,S} {14,S} {15,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(4375)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
        2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
        3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
        5  C u0 p0 c0 {3,S} {8,S} {16,S} {17,S}
        6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
        7  O u0 p2 c0 {1,S} {8,S}
        8  O u0 p2 c0 {5,S} {7,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {2,S}
        15 H u0 p0 c0 {2,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {5,S}
        18 H u0 p0 c0 {6,S}
        19 H u0 p0 c0 {6,S}
        20 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(4374)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
        5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {4,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(317)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,D} {7,S}
        3  C u0 p0 c0 {2,D} {8,S} {9,S}
        4  O u0 p2 c0 {1,S} {10,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 O u1 p2 c0 {4,S}
        """),
)
            
species(
    label='S(10859)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
        2  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
        3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
        4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
        5  C u0 p0 c0 {1,S} {6,D} {19,S}
        6  C u0 p0 c0 {2,S} {5,D} {18,S}
        7  O u0 p2 c0 {3,S} {8,S}
        8  O u0 p2 c0 {7,S} {20,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {6,S}
        19 H u0 p0 c0 {5,S}
        20 H u0 p0 c0 {8,S}
        """),
)
            
species(
    label='S(1190)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {14,S} {15,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(11276)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
        4  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
        6  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
        7  O u0 p2 c0 {2,S} {8,S}
        8  O u0 p2 c0 {7,S} {20,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 H u0 p0 c0 {6,S}
        20 H u0 p0 c0 {8,S}
        """),
)
            
species(
    label='S(1608)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
        5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(11776)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
        2  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
        3  C u0 p0 c0 {2,S} {13,S} {14,S} {18,S}
        4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
        5  C u0 p0 c0 {1,S} {6,D} {7,S}
        6  C u0 p0 c0 {2,S} {5,D} {19,S}
        7  O u0 p2 c0 {5,S} {8,S}
        8  O u0 p2 c0 {7,S} {20,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {3,S}
        19 H u0 p0 c0 {6,S}
        20 H u0 p0 c0 {8,S}
        """),
)
            
species(
    label='S(5512)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(12549)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
        2  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
        3  C u0 p0 c0 {2,S} {11,S} {12,S} {16,S}
        4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {1,S} {6,S} {18,D}
        6  C u1 p0 c0 {2,S} {5,S} {17,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {3,S}
        17 H u0 p0 c0 {6,S}
        18 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(6062)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {14,S} {15,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(1192)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {5,D} {15,S}
        5  C u0 p0 c0 {3,S} {4,D} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(13393)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {13,S} {14,S} {18,S}
        5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
        6  C u0 p0 c0 {1,S} {3,S} {19,D}
        7  O u0 p2 c0 {1,S} {20,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {5,S}
        18 H u0 p0 c0 {4,S}
        19 O u0 p2 c0 {6,D}
        20 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(14200)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
        3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {6,S} {13,D}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {4,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='S(1191)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {4,D} {14,S} {15,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(14937)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {3,D} {10,S}
        3  C u0 p0 c0 {2,D} {5,S} {11,S}
        4  C u0 p0 c0 {6,S} {12,D} {13,S}
        5  O u0 p2 c0 {3,S} {6,S}
        6  O u0 p2 c0 {4,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 O u0 p2 c0 {4,D}
        13 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(5513)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(15753)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {6,S} {13,D}
        5  O u0 p2 c0 {2,S} {6,S}
        6  O u0 p2 c0 {4,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='S(4168)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
        5  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {4,S}
        8  H u0 p0 c0 {4,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(100)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
        3 O u0 p2 c0 {1,S} {4,S}
        4 O u0 p2 c0 {1,S} {3,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='C3H5O(109)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2 C u1 p0 c0 {1,S} {3,S} {7,S}
        3 C u0 p0 c0 {2,S} {8,S} {9,D}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {3,S}
        9 O u0 p2 c0 {3,D}
        """),
)
            
species(
    label='S(157)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
        3 O u1 p2 c0 {2,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 O u1 p2 c0 {2,S}
        8 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='C3H6O(106)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  O u0 p2 c0 {1,S} {10,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(328)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {9,S} {10,D}
        4  O u0 p2 c0 {1,S} {11,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 O u0 p2 c0 {3,D}
        11 O u1 p2 c0 {4,S}
        """),
)
            
species(
    label='S(2201)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {4,S} {6,S} {12,D}
        4  C u1 p0 c0 {3,S} {13,S} {14,S}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {3,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 O u0 p2 c0 {3,D}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(2306)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,D}
        2 C u1 p0 c0 {1,S} {5,S} {6,S}
        3 O u0 p2 c0 {1,S} {7,S}
        4 O u0 p2 c0 {1,D}
        5 H u0 p0 c0 {2,S}
        6 H u0 p0 c0 {2,S}
        7 O u1 p2 c0 {3,S}
        """),
)
            
species(
    label='S(3861)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
        2  C u1 p0 c0 {1,S} {3,S} {8,S}
        3  C u0 p0 c0 {2,S} {4,S} {9,D}
        4  O u0 p2 c0 {3,S} {10,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  O u0 p2 c0 {3,D}
        10 O u1 p2 c0 {4,S}
        """),
)
            
species(
    label='S(1312)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {3,S} {5,S} {9,D}
        3  C u1 p0 c0 {2,S} {10,S} {11,S}
        4  O u0 p2 c0 {1,S} {5,S}
        5  O u0 p2 c0 {2,S} {4,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  O u0 p2 c0 {2,D}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='S(30668)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {5,S} {12,D}
        4  O u0 p2 c0 {2,S} {5,S}
        5  O u0 p2 c0 {3,S} {4,S}
        6  O u0 p2 c0 {1,S} {13,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 O u0 p2 c0 {3,D}
        13 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(455)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {3,S} {6,D}
        3 O u0 p2 c0 {1,S} {2,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 O u0 p2 c0 {2,D}
        """),
)
            
species(
    label='S(3946)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {3,D} {4,S} {5,S}
        2 C u0 p0 c0 {3,D} {6,S} {7,S}
        3 C u0 p0 c0 {1,D} {2,D}
        4 O u0 p2 c0 {1,S} {8,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        8 O u1 p2 c0 {4,S}
        """),
)
            
species(
    label='S(15245)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {3,D} {9,S}
        3  C u0 p0 c0 {2,D} {10,S} {11,S}
        4  C u0 p0 c0 {6,S} {12,S} {13,D}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {4,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='S(352)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {9,D} {10,S}
        4  H u0 p0 c0 {1,S}
        5  H u0 p0 c0 {1,S}
        6  O u1 p2 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  O u0 p2 c0 {3,D}
        10 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='S(3944)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2 C u0 p0 c0 {1,S} {4,T}
        3 O u0 p2 c0 {1,S} {7,S}
        4 C u0 p0 c0 {2,T} {8,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 O u1 p2 c0 {3,S}
        8 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(283)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {6,S} {7,D}
        3 O u0 p2 c0 {1,S} {8,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 O u0 p2 c0 {2,D}
        8 O u1 p2 c0 {3,S}
        """),
)
            
species(
    label='CH2O2(71)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u1 p0 c0 {2,S} {3,S} {4,S}
        2 O u0 p2 c0 {1,S} {5,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 O u1 p2 c0 {2,S}
        """),
)
            
species(
    label='CHO3(266)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,D}
        2 O u0 p2 c0 {1,S} {5,S}
        3 H u0 p0 c0 {1,S}
        4 O u0 p2 c0 {1,D}
        5 O u1 p2 c0 {2,S}
        """),
)
            
species(
    label='S(25890)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
        2  C u0 p0 c0 {5,S} {8,S} {16,S} {17,S}
        3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        4  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
        5  C u1 p0 c0 {2,S} {4,S} {21,S}
        6  C u0 p0 c0 {9,S} {10,S} {22,D}
        7  O u0 p2 c0 {1,S} {9,S}
        8  O u0 p2 c0 {2,S} {10,S}
        9  O u0 p2 c0 {6,S} {7,S}
        10 O u0 p2 c0 {6,S} {8,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {1,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {2,S}
        17 H u0 p0 c0 {2,S}
        18 H u0 p0 c0 {4,S}
        19 H u0 p0 c0 {4,S}
        20 H u0 p0 c0 {4,S}
        21 H u0 p0 c0 {5,S}
        22 O u0 p2 c0 {6,D}
        """),
)
            
species(
    label='S(25615)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
        2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
        3  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
        4  C u1 p0 c0 {1,S} {2,S} {18,S}
        5  C u0 p0 c0 {8,S} {9,S} {19,D}
        6  O u0 p2 c0 {1,S} {9,S}
        7  O u0 p2 c0 {3,S} {8,S}
        8  O u0 p2 c0 {5,S} {7,S}
        9  O u0 p2 c0 {5,S} {6,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {2,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {3,S}
        17 H u0 p0 c0 {3,S}
        18 H u0 p0 c0 {4,S}
        19 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(36855)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {6,S} {13,D}
        5  O u0 p2 c0 {3,S} {6,S}
        6  O u0 p2 c0 {4,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='S(40212)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,D} {9,S}
        3  C u0 p0 c0 {1,S} {5,S} {10,D}
        4  C u0 p0 c0 {2,D} {11,S} {12,S}
        5  O u0 p2 c0 {3,S} {6,S}
        6  O u0 p2 c0 {5,S} {13,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 O u0 p2 c0 {3,D}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(161)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u1 p0 c0 {2,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {3,S} {6,D}
        3 O u1 p2 c0 {2,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 O u0 p2 c0 {2,D}
        """),
)
            
species(
    label='S(41743)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {9,S} {12,S}
        2  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
        3  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
        4  C u0 p0 c0 {1,S} {20,S} {21,S} {22,S}
        5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
        6  C u0 p0 c0 {10,S} {11,S} {23,D}
        7  O u0 p2 c0 {3,S} {10,S}
        8  O u0 p2 c0 {2,S} {11,S}
        9  O u0 p2 c0 {1,S} {24,S}
        10 O u0 p2 c0 {6,S} {7,S}
        11 O u0 p2 c0 {6,S} {8,S}
        12 H u0 p0 c0 {1,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {2,S}
        16 H u0 p0 c0 {2,S}
        17 H u0 p0 c0 {5,S}
        18 H u0 p0 c0 {5,S}
        19 H u0 p0 c0 {5,S}
        20 H u0 p0 c0 {4,S}
        21 H u0 p0 c0 {4,S}
        22 H u0 p0 c0 {4,S}
        23 O u0 p2 c0 {6,D}
        24 O u1 p2 c0 {9,S}
        """),
)
            
species(
    label='S(41745)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {8,S} {11,S}
        2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
        3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
        4  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
        5  C u0 p0 c0 {9,S} {10,S} {20,D}
        6  O u0 p2 c0 {2,S} {10,S}
        7  O u0 p2 c0 {4,S} {9,S}
        8  O u0 p2 c0 {1,S} {21,S}
        9  O u0 p2 c0 {5,S} {7,S}
        10 O u0 p2 c0 {5,S} {6,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {3,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {4,S}
        19 H u0 p0 c0 {4,S}
        20 O u0 p2 c0 {5,D}
        21 O u1 p2 c0 {8,S}
        """),
)
            
species(
    label='S(15754)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {6,S} {13,D}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {4,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='C2H4O(72)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u1 p0 c0 {1,S} {6,S} {7,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 O u1 p2 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='S(29217)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,D}
        2  C u1 p0 c0 {1,S} {7,S} {8,S}
        3  C u0 p0 c0 {5,S} {9,S} {10,D}
        4  O u0 p2 c0 {1,S} {5,S}
        5  O u0 p2 c0 {3,S} {4,S}
        6  O u0 p2 c0 {1,D}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 O u0 p2 c0 {3,D}
        """),
)
            
species(
    label='S(2355)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {5,S} {10,D}
        3  C u0 p0 c0 {4,D} {6,S} {11,S}
        4  C u0 p0 c0 {3,D} {12,S} {13,S}
        5  O u0 p2 c0 {2,S} {6,S}
        6  O u0 p2 c0 {3,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 O u0 p2 c0 {2,D}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(34572)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,D}
        3  C u0 p0 c0 {6,S} {10,D} {11,S}
        4  O u0 p2 c0 {2,S} {6,S}
        5  O u0 p2 c0 {1,S} {12,S}
        6  O u0 p2 c0 {3,S} {4,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  O u0 p2 c0 {2,D}
        10 O u0 p2 c0 {3,D}
        11 H u0 p0 c0 {3,S}
        12 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(40267)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {12,S}
        2  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
        3  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
        4  C u0 p0 c0 {8,S} {18,S} {19,S} {20,S}
        5  C u0 p0 c0 {9,S} {10,S} {21,D}
        6  O u0 p2 c0 {1,S} {11,S}
        7  O u0 p2 c0 {2,S} {10,S}
        8  O u0 p2 c0 {4,S} {9,S}
        9  O u0 p2 c0 {5,S} {8,S}
        10 O u0 p2 c0 {5,S} {7,S}
        11 O u0 p2 c0 {6,S} {22,S}
        12 H u0 p0 c0 {1,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {2,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {3,S}
        17 H u0 p0 c0 {3,S}
        18 H u0 p0 c0 {4,S}
        19 H u0 p0 c0 {4,S}
        20 H u0 p0 c0 {4,S}
        21 O u0 p2 c0 {5,D}
        22 H u0 p0 c0 {11,S}
        """),
)
            
species(
    label='S(16856)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {5,S} {12,D}
        4  C u0 p0 c0 {6,S} {13,S} {14,D}
        5  O u0 p2 c0 {3,S} {6,S}
        6  O u0 p2 c0 {4,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  O u1 p2 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 O u0 p2 c0 {3,D}
        13 H u0 p0 c0 {4,S}
        14 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='S(40184)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
        2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {5,S} {7,S} {14,D}
        5  O u0 p2 c0 {1,S} {4,S}
        6  O u0 p2 c0 {2,S} {7,S}
        7  O u0 p2 c0 {4,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='S(5237)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
        5  C u0 p0 c0 {6,S} {14,S} {18,S} {19,S}
        6  C u1 p0 c0 {2,S} {4,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {5,S}
        19 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(40264)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {13,S}
        2  C u0 p0 c0 {1,S} {9,S} {16,S} {17,S}
        3  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
        4  C u0 p0 c0 {1,S} {21,S} {22,S} {23,S}
        5  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
        6  C u0 p0 c0 {10,S} {11,S} {24,D}
        7  O u0 p2 c0 {1,S} {12,S}
        8  O u0 p2 c0 {3,S} {10,S}
        9  O u0 p2 c0 {2,S} {11,S}
        10 O u0 p2 c0 {6,S} {8,S}
        11 O u0 p2 c0 {6,S} {9,S}
        12 O u0 p2 c0 {7,S} {25,S}
        13 H u0 p0 c0 {1,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {2,S}
        17 H u0 p0 c0 {2,S}
        18 H u0 p0 c0 {5,S}
        19 H u0 p0 c0 {5,S}
        20 H u0 p0 c0 {5,S}
        21 H u0 p0 c0 {4,S}
        22 H u0 p0 c0 {4,S}
        23 H u0 p0 c0 {4,S}
        24 O u0 p2 c0 {6,D}
        25 H u0 p0 c0 {12,S}
        """),
)
            
species(
    label='CH2O3(272)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {4,D} {5,S}
        2 O u0 p2 c0 {1,S} {3,S}
        3 O u0 p2 c0 {2,S} {6,S}
        4 O u0 p2 c0 {1,D}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='S(59047)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
        2  C u0 p0 c0 {1,S} {3,D} {5,S}
        3  C u0 p0 c0 {2,D} {11,S} {12,S}
        4  C u0 p0 c0 {5,S} {6,S} {13,D}
        5  O u0 p2 c0 {2,S} {4,S}
        6  O u0 p2 c0 {4,S} {7,S}
        7  O u0 p2 c0 {6,S} {14,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 O u0 p2 c0 {4,D}
        14 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='C4H8(994)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {2,S} {4,D}
        4  C u0 p0 c0 {3,D} {11,S} {12,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(62542)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {5,S} {7,S} {14,D}
        5  O u0 p2 c0 {1,S} {4,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {4,S} {6,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='C4H9(8484)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {5,S} {6,S} {8,S}
        2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
        4  C u1 p0 c0 {1,S} {2,S} {3,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {3,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='S(48514)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,D} {8,S}
        3  C u0 p0 c0 {2,D} {5,S} {9,S}
        4  O u0 p2 c0 {1,S} {5,S}
        5  O u0 p2 c0 {3,S} {4,S}
        6  O u0 p2 c0 {1,S} {10,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  O u1 p2 c0 {3,S}
        10 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(62581)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
        5  O u0 p2 c0 {1,S} {15,S}
        6  H u0 p0 c0 {4,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(65019)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
        2  C u0 p0 c0 {1,S} {3,D} {5,S}
        3  C u0 p0 c0 {2,D} {11,S} {12,S}
        4  C u0 p0 c0 {6,S} {7,S} {13,D}
        5  O u0 p2 c0 {2,S} {6,S}
        6  O u0 p2 c0 {4,S} {5,S}
        7  O u0 p2 c0 {4,S} {14,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 O u0 p2 c0 {4,D}
        14 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='CHO3(154)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,D}
        2 O u0 p2 c0 {1,S} {5,S}
        3 O u1 p2 c0 {1,S}
        4 O u0 p2 c0 {1,D}
        5 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='S(23143)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
        4  C u0 p0 c0 {5,S} {11,S} {15,S} {16,S}
        5  C u1 p0 c0 {1,S} {3,S} {4,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(69792)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
        2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {5,S} {7,S} {14,D}
        5  O u0 p2 c0 {2,S} {4,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {4,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='C2H3O(86)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,D} {4,S} {5,S}
        2 C u1 p0 c0 {1,D} {3,S}
        3 O u0 p2 c0 {2,S} {6,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C4H7(990)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {4,D}
        3  C u1 p0 c0 {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {2,D} {10,S} {11,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(63143)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
        2  C u0 p0 c0 {1,S} {3,D} {11,S}
        3  C u0 p0 c0 {2,D} {5,S} {12,S}
        4  C u0 p0 c0 {5,S} {6,S} {13,D}
        5  O u0 p2 c0 {3,S} {4,S}
        6  O u0 p2 c0 {4,S} {7,S}
        7  O u0 p2 c0 {6,S} {14,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 O u0 p2 c0 {4,D}
        14 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(17086)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {2,S} {4,D}
        4  C u0 p0 c0 {3,D} {11,S} {12,S}
        5  O u0 p2 c0 {1,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(75285)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {5,S} {7,S} {14,D}
        5  O u0 p2 c0 {2,S} {4,S}
        6  O u0 p2 c0 {2,S} {7,S}
        7  O u0 p2 c0 {4,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='S(3721)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,D} {4,S}
        2 C u1 p0 c0 {1,S} {5,S} {6,S}
        3 C u0 p0 c0 {1,D} {7,S} {8,S}
        4 O u0 p2 c0 {1,S} {9,S}
        5 H u0 p0 c0 {2,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {3,S}
        8 H u0 p0 c0 {3,S}
        9 O u1 p2 c0 {4,S}
        """),
)
            
species(
    label='S(24432)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
        2  C u0 p0 c0 {1,S} {3,D} {11,S}
        3  C u0 p0 c0 {2,D} {5,S} {12,S}
        4  C u0 p0 c0 {6,S} {7,S} {13,D}
        5  O u0 p2 c0 {3,S} {6,S}
        6  O u0 p2 c0 {4,S} {5,S}
        7  O u0 p2 c0 {4,S} {14,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 O u0 p2 c0 {4,D}
        14 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(78865)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
        2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
        3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
        4  C u1 p0 c0 {1,S} {2,S} {3,S}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {2,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='S(36871)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
        2 C u0 p0 c0 {3,D} {5,S} {8,S}
        3 C u1 p0 c0 {1,S} {2,D}
        4 O u0 p2 c0 {1,S} {5,S}
        5 O u0 p2 c0 {2,S} {4,S}
        6 H u0 p0 c0 {1,S}
        7 H u0 p0 c0 {1,S}
        8 H u0 p0 c0 {2,S}
        """),
)
            
species(
    label='S(75316)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
        2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {2,S} {4,D}
        4  C u0 p0 c0 {3,D} {12,S} {13,S}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {5,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(17025)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {3,D} {10,S}
        3  C u0 p0 c0 {2,D} {12,S} {13,S}
        4  C u0 p0 c0 {6,S} {7,S} {11,D}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {4,S} {5,S}
        7  O u0 p2 c0 {4,S} {14,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 O u0 p2 c0 {4,D}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(81568)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        5  O u0 p2 c0 {2,S} {6,S}
        6  O u0 p2 c0 {3,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(82419)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        5  O u0 p2 c0 {2,S} {6,S}
        6  O u0 p2 c0 {3,S} {5,S}
        7  O u0 p2 c0 {1,S} {15,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(85509)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {2,S} {5,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(89559)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {1,S} {2,S} {4,D}
        4  C u0 p0 c0 {3,D} {5,S} {13,S}
        5  O u0 p2 c0 {4,S} {6,S}
        6  O u0 p2 c0 {5,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(85513)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
        3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
        4  C u0 p0 c0 {5,S} {7,S} {14,D}
        5  O u0 p2 c0 {2,S} {4,S}
        6  O u0 p2 c0 {3,S} {7,S}
        7  O u0 p2 c0 {4,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='S(26541)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
        2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {2,S} {4,D}
        4  C u0 p0 c0 {3,D} {11,S} {12,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {4,S}
        12 O u1 p2 c0 {4,S}
        """),
)
            
species(
    label='S(28084)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {12,S} {13,D}
        5  O u0 p2 c0 {1,S} {14,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 O u0 p2 c0 {4,D}
        14 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(16116)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
        2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        3  C u0 p0 c0 {4,S} {7,S} {15,S} {16,S}
        4  C u1 p0 c0 {3,S} {17,S} {18,S}
        5  C u0 p0 c0 {8,S} {9,S} {19,D}
        6  O u0 p2 c0 {1,S} {8,S}
        7  O u0 p2 c0 {3,S} {9,S}
        8  O u0 p2 c0 {5,S} {6,S}
        9  O u0 p2 c0 {5,S} {7,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {2,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {3,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {4,S}
        19 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(63117)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {4,D} {10,S}
        3  C u0 p0 c0 {5,S} {6,S} {11,D}
        4  C u0 p0 c0 {2,D} {12,S} {13,S}
        5  O u0 p2 c0 {1,S} {3,S}
        6  O u0 p2 c0 {3,S} {7,S}
        7  O u0 p2 c0 {6,S} {14,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 O u0 p2 c0 {3,D}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='C4H6O(412)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {4,D}
        3  C u0 p0 c0 {2,S} {8,D} {9,S}
        4  C u0 p0 c0 {2,D} {10,S} {11,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  O u0 p2 c0 {3,D}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(59054)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
        3  C u0 p0 c0 {4,S} {6,S} {11,D}
        4  O u0 p2 c0 {1,S} {3,S}
        5  O u0 p2 c0 {2,S} {6,S}
        6  O u0 p2 c0 {3,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 O u0 p2 c0 {3,D}
        """),
)
            
species(
    label='S(96372)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {4,D}
        4  C u0 p0 c0 {3,D} {9,S} {10,S}
        5  O u0 p2 c0 {1,S} {11,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(62538)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,D} {4,S} {7,S}
        2  C u0 p0 c0 {4,S} {5,S} {8,D}
        3  C u0 p0 c0 {1,D} {9,S} {10,S}
        4  O u0 p2 c0 {1,S} {2,S}
        5  O u0 p2 c0 {2,S} {6,S}
        6  O u0 p2 c0 {5,S} {11,S}
        7  H u0 p0 c0 {1,S}
        8  O u0 p2 c0 {2,D}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(1286)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {5,T}
        4  O u0 p2 c0 {2,S} {10,S}
        5  C u0 p0 c0 {3,T} {11,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(105546)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,D} {5,S}
        4  C u0 p0 c0 {3,D} {10,S} {11,S}
        5  O u0 p2 c0 {2,S} {3,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(65017)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {4,S} {6,S} {11,D}
        4  O u0 p2 c0 {1,S} {3,S}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {3,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 O u0 p2 c0 {3,D}
        """),
)
            
species(
    label='S(736)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,D} {4,S} {7,S}
        2  C u0 p0 c0 {5,S} {6,S} {8,D}
        3  C u0 p0 c0 {1,D} {9,S} {10,S}
        4  O u0 p2 c0 {1,S} {5,S}
        5  O u0 p2 c0 {2,S} {4,S}
        6  O u0 p2 c0 {2,S} {11,S}
        7  H u0 p0 c0 {1,S}
        8  O u0 p2 c0 {2,D}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(75480)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,D} {5,S}
        2  C u0 p0 c0 {1,S} {4,D} {6,S}
        3  C u0 p0 c0 {1,D} {9,S} {10,S}
        4  C u0 p0 c0 {2,D} {7,S} {8,S}
        5  O u0 p2 c0 {1,S} {11,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {4,S}
        8  H u0 p0 c0 {4,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(15674)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
        2  C u1 p0 c0 {1,S} {10,S} {11,S}
        3  C u0 p0 c0 {5,S} {6,S} {12,D}
        4  O u0 p2 c0 {1,S} {5,S}
        5  O u0 p2 c0 {3,S} {4,S}
        6  O u0 p2 c0 {3,S} {7,S}
        7  O u0 p2 c0 {6,S} {13,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 O u0 p2 c0 {3,D}
        13 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(112116)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,D} {5,S}
        4  C u0 p0 c0 {2,S} {3,D} {10,S}
        5  O u0 p2 c0 {3,S} {11,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(40524)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
        2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
        3  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
        4  C u1 p0 c0 {1,S} {17,S} {18,S}
        5  C u0 p0 c0 {8,S} {9,S} {19,D}
        6  O u0 p2 c0 {2,S} {9,S}
        7  O u0 p2 c0 {3,S} {8,S}
        8  O u0 p2 c0 {5,S} {7,S}
        9  O u0 p2 c0 {5,S} {6,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {3,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {4,S}
        19 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(1658)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,D} {7,S}
        2  C u0 p0 c0 {1,S} {4,D} {6,S}
        3  C u0 p0 c0 {1,D} {5,S} {8,S}
        4  C u0 p0 c0 {2,D} {9,S} {10,S}
        5  O u0 p2 c0 {3,S} {11,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(466)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
        2 C u0 p0 c0 {4,S} {8,S} {9,D}
        3 O u0 p2 c0 {1,S} {4,S}
        4 O u0 p2 c0 {2,S} {3,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 H u0 p0 c0 {1,S}
        8 O u1 p2 c0 {2,S}
        9 O u0 p2 c0 {2,D}
        """),
)
            
species(
    label='S(121749)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,D} {10,S}
        4  C u0 p0 c0 {3,D} {5,S} {11,S}
        5  O u0 p2 c0 {2,S} {4,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='C3H6O(787)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        4  O u0 p2 c0 {2,S} {3,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C3H6O(243)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,D} {7,S}
        3  C u0 p0 c0 {2,D} {8,S} {9,S}
        4  O u0 p2 c0 {1,S} {10,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(112117)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,D} {9,S}
        4  C u0 p0 c0 {2,S} {3,D} {10,S}
        5  O u0 p2 c0 {1,S} {11,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='C4H6O(413)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,D} {8,S}
        3  C u0 p0 c0 {2,D} {4,S} {9,S}
        4  C u0 p0 c0 {3,S} {10,D} {11,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 O u0 p2 c0 {4,D}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='C3H6O(978)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        4  O u0 p2 c0 {1,S} {2,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C3H6O(107)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {3,D} {4,S} {8,S}
        3  C u0 p0 c0 {2,D} {9,S} {10,S}
        4  O u0 p2 c0 {1,S} {2,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='C4H6O(411)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,D} {7,S}
        3  C u0 p0 c0 {1,S} {8,D} {9,S}
        4  C u0 p0 c0 {2,D} {10,S} {11,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  O u0 p2 c0 {3,D}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(44008)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
        2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        3  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
        4  C u0 p0 c0 {7,S} {8,S} {17,D}
        5  O u0 p2 c0 {1,S} {7,S}
        6  O u0 p2 c0 {3,S} {8,S}
        7  O u0 p2 c0 {4,S} {5,S}
        8  O u0 p2 c0 {4,S} {6,S}
        9  O u1 p2 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {3,S}
        17 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='S(1572)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        4  C u0 p0 c0 {2,S} {3,S} {11,D}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='C4H6O(414)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,D}
        3  C u0 p0 c0 {2,S} {4,D} {9,S}
        4  C u0 p0 c0 {3,D} {10,S} {11,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  O u0 p2 c0 {2,D}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(40399)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
        2  C u0 p0 c0 {5,S} {6,S} {11,D}
        3  C u0 p0 c0 {7,S} {12,D} {13,S}
        4  O u0 p2 c0 {1,S} {5,S}
        5  O u0 p2 c0 {2,S} {4,S}
        6  O u0 p2 c0 {2,S} {7,S}
        7  O u0 p2 c0 {3,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 O u0 p2 c0 {2,D}
        12 O u0 p2 c0 {3,D}
        13 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='S(1072)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,D} {10,S}
        4  C u0 p0 c0 {3,D} {11,D}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='S(35381)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {3,S} {4,S} {5,D}
        2 C u1 p0 c0 {3,S} {6,S} {7,S}
        3 O u0 p2 c0 {1,S} {2,S}
        4 O u0 p2 c0 {1,S} {8,S}
        5 O u0 p2 c0 {1,D}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        8 O u1 p2 c0 {4,S}
        """),
)
            
species(
    label='S(108598)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
        2 C u0 p0 c0 {3,S} {5,S} {8,D}
        3 O u0 p2 c0 {1,S} {2,S}
        4 O u0 p2 c0 {1,S} {5,S}
        5 O u0 p2 c0 {2,S} {4,S}
        6 H u0 p0 c0 {1,S}
        7 H u0 p0 c0 {1,S}
        8 O u0 p2 c0 {2,D}
        """),
)
            
species(
    label='S(1077)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {10,D} {11,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 O u0 p2 c0 {4,D}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(1071)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {2,S} {11,D}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='S(53640)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,S} {10,D}
        4  O u0 p2 c0 {2,S} {5,S}
        5  O u0 p2 c0 {3,S} {4,S}
        6  O u0 p2 c0 {1,S} {12,S}
        7  O u0 p2 c0 {2,S} {11,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 O u0 p2 c0 {3,D}
        11 H u0 p0 c0 {7,S}
        12 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(110630)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
        2  C u0 p0 c0 {5,S} {8,S} {15,S} {16,S}
        3  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
        4  C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
        5  C u0 p0 c0 {2,S} {10,S} {23,D}
        6  C u0 p0 c0 {11,S} {12,S} {24,D}
        7  O u0 p2 c0 {1,S} {12,S}
        8  O u0 p2 c0 {2,S} {11,S}
        9  O u0 p2 c0 {4,S} {10,S}
        10 O u0 p2 c0 {5,S} {9,S}
        11 O u0 p2 c0 {6,S} {8,S}
        12 O u0 p2 c0 {6,S} {7,S}
        13 O u1 p2 c0 {1,S}
        14 H u0 p0 c0 {1,S}
        15 H u0 p0 c0 {2,S}
        16 H u0 p0 c0 {2,S}
        17 H u0 p0 c0 {3,S}
        18 H u0 p0 c0 {3,S}
        19 H u0 p0 c0 {3,S}
        20 H u0 p0 c0 {4,S}
        21 H u0 p0 c0 {4,S}
        22 H u0 p0 c0 {4,S}
        23 O u0 p2 c0 {5,D}
        24 O u0 p2 c0 {6,D}
        """),
)
            
species(
    label='S(1638)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,D} {5,S} {6,S}
        2  C u0 p0 c0 {4,D} {5,S} {7,S}
        3  C u0 p0 c0 {1,D} {8,S} {9,S}
        4  C u0 p0 c0 {2,D} {10,S} {11,S}
        5  O u0 p2 c0 {1,S} {2,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(23134)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u1 p0 c0 {1,S} {4,S} {11,S}
        4  C u0 p0 c0 {3,S} {5,S} {12,D}
        5  O u0 p2 c0 {4,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 O u0 p2 c0 {4,D}
        13 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(141973)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
        2  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
        3  C u0 p0 c0 {1,S} {8,S} {17,D}
        4  C u0 p0 c0 {9,S} {10,S} {18,D}
        5  C u0 p0 c0 {11,S} {19,S} {20,D}
        6  O u0 p2 c0 {1,S} {9,S}
        7  O u0 p2 c0 {2,S} {8,S}
        8  O u0 p2 c0 {3,S} {7,S}
        9  O u0 p2 c0 {4,S} {6,S}
        10 O u0 p2 c0 {4,S} {11,S}
        11 O u0 p2 c0 {5,S} {10,S}
        12 H u0 p0 c0 {1,S}
        13 H u0 p0 c0 {1,S}
        14 H u0 p0 c0 {2,S}
        15 H u0 p0 c0 {2,S}
        16 H u0 p0 c0 {2,S}
        17 O u0 p2 c0 {3,D}
        18 O u0 p2 c0 {4,D}
        19 H u0 p0 c0 {5,S}
        20 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(121753)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,D} {10,S}
        4  C u0 p0 c0 {3,D} {5,S} {11,S}
        5  O u0 p2 c0 {1,S} {4,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='C5H9(4366)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
        4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
        5  C u1 p0 c0 {3,S} {4,S} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(15794)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
        2  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
        3  C u1 p0 c0 {1,S} {14,S} {15,S}
        4  C u0 p0 c0 {7,S} {8,S} {16,D}
        5  O u0 p2 c0 {1,S} {8,S}
        6  O u0 p2 c0 {2,S} {7,S}
        7  O u0 p2 c0 {4,S} {6,S}
        8  O u0 p2 c0 {4,S} {5,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='S(167117)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
        3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
        4  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
        5  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
        6  O u0 p2 c0 {1,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {4,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {5,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(11645)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
        2  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
        3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {14,S} {15,S}
        6  O u0 p2 c0 {1,S} {16,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(2409)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
        5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        6  O u0 p2 c0 {2,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='C5H9(7114)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u1 p0 c0 {1,S} {4,S} {11,S}
        4  C u0 p0 c0 {3,S} {5,D} {12,S}
        5  C u0 p0 c0 {4,D} {13,S} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(11658)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
        4  C u0 p0 c0 {1,S} {5,D} {6,S}
        5  C u0 p0 c0 {3,S} {4,D} {15,S}
        6  O u0 p2 c0 {4,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(174496)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {5,D} {14,S}
        5  C u0 p0 c0 {3,S} {4,D} {15,S}
        6  O u0 p2 c0 {3,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(178557)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {5,S} {9,S} {12,S}
        5  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
        6  O u0 p2 c0 {1,S} {16,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='C4H6(1635)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,D} {5,S}
        2  C u0 p0 c0 {1,S} {4,D} {6,S}
        3  C u0 p0 c0 {1,D} {7,S} {8,S}
        4  C u0 p0 c0 {2,D} {9,S} {10,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {3,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(173764)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,D} {9,S}
        4  C u0 p0 c0 {2,S} {3,D} {10,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(10803)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
        3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {5,D} {15,S}
        5  C u0 p0 c0 {3,S} {4,D} {14,S}
        6  O u0 p2 c0 {2,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {4,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(184362)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
        3  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
        4  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {3,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(173749)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {5,D} {6,S}
        5  C u0 p0 c0 {4,D} {14,S} {15,S}
        6  O u0 p2 c0 {4,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='C4H6(1067)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {4,D}
        4  C u0 p0 c0 {3,D} {9,S} {10,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(186823)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
        5  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
        6  O u0 p2 c0 {1,S} {16,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(189050)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {10,S}
        3  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {14,S} {15,S}
        6  O u0 p2 c0 {1,S} {16,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='C4H6(1006)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,T}
        4  C u0 p0 c0 {3,T} {10,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(192235)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,S} {7,S} {10,S}
        4  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        6  O u0 p2 c0 {1,S} {16,S}
        7  H u0 p0 c0 {3,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='C5H9(7421)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {2,S} {4,D}
        4  C u0 p0 c0 {3,D} {5,S} {12,S}
        5  C u1 p0 c0 {4,S} {13,S} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(181895)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,D} {9,S}
        4  C u0 p0 c0 {1,S} {3,D} {10,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(195070)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
        4  C u0 p0 c0 {3,S} {5,D} {6,S}
        5  C u0 p0 c0 {1,S} {4,D} {15,S}
        6  O u0 p2 c0 {4,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(195845)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
        4  C u0 p0 c0 {2,S} {3,S} {5,D}
        5  C u0 p0 c0 {1,S} {4,D} {15,S}
        6  O u0 p2 c0 {1,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(112121)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,D} {5,S}
        4  C u0 p0 c0 {3,D} {10,S} {11,S}
        5  O u0 p2 c0 {1,S} {3,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(139848)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,D} {5,S}
        3  C u0 p0 c0 {4,D} {9,S} {10,S}
        4  C u0 p0 c0 {2,D} {3,D}
        5  O u0 p2 c0 {2,S} {11,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(26814)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {14,S} {15,S}
        6  O u0 p2 c0 {1,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(2482)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,T}
        4  O u0 p2 c0 {1,S} {10,S}
        5  C u0 p0 c0 {3,T} {11,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(172113)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {5,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {6,S} {9,S}
        4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        5  C u0 p0 c0 {2,S} {10,S} {14,S} {15,S}
        6  O u0 p2 c0 {3,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {5,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(200518)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
        5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
        6  O u0 p2 c0 {2,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(173760)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,D} {5,S}
        2  C u1 p0 c0 {1,S} {4,S} {6,S}
        3  C u0 p0 c0 {1,D} {7,S} {8,S}
        4  C u1 p0 c0 {2,S} {9,S} {10,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {3,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(1036)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
        2  C u1 p0 c0 {1,S} {3,S} {8,S}
        3  C u0 p0 c0 {2,S} {4,S} {9,D}
        4  C u1 p0 c0 {3,S} {10,S} {11,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  O u0 p2 c0 {3,D}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='C1OO1(94)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 O u0 p2 c0 {1,S} {3,S}
        3 O u0 p2 c0 {1,S} {2,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='CH2O2(155)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 O u1 p2 c0 {1,S}
        3 O u1 p2 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        """),
)
            
species(
    label='S(81708)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {2,S} {5,D} {6,S}
        5  C u0 p0 c0 {4,D} {14,S} {15,S}
        6  O u0 p2 c0 {4,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(1070)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,D} {5,S}
        4  C u0 p0 c0 {2,S} {3,D} {11,S}
        5  O u0 p2 c0 {1,S} {3,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(220152)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,T}
        4  C u0 p0 c0 {2,S} {3,T}
        5  O u0 p2 c0 {1,S} {11,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(2408)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
        2  C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        6  O u0 p2 c0 {2,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(26832)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {5,D} {15,S}
        5  C u0 p0 c0 {3,S} {4,D} {14,S}
        6  O u0 p2 c0 {1,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {4,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='C4H6(1030)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,D}
        2  C u1 p0 c0 {1,S} {5,S} {6,S}
        3  C u1 p0 c0 {1,S} {7,S} {8,S}
        4  C u0 p0 c0 {1,D} {9,S} {10,S}
        5  H u0 p0 c0 {2,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {3,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='C4H7(1034)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,D} {8,S}
        3  C u0 p0 c0 {2,D} {4,S} {9,S}
        4  C u1 p0 c0 {3,S} {10,S} {11,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(17085)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,D} {10,S}
        4  C u0 p0 c0 {3,D} {11,S} {12,S}
        5  O u0 p2 c0 {1,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='C5H9(7997)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {5,D} {12,S}
        4  C u1 p0 c0 {2,S} {5,S} {13,S}
        5  C u0 p0 c0 {3,D} {4,S} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(184364)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
        5  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
        6  O u0 p2 c0 {2,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(17087)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,D} {11,S}
        4  C u0 p0 c0 {2,S} {3,D} {12,S}
        5  O u0 p2 c0 {1,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(173748)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {4,D} {6,S} {15,S}
        6  O u0 p2 c0 {5,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(189049)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        5  O u0 p2 c0 {2,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(77794)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
        3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {4,D} {14,S} {15,S}
        6  O u0 p2 c0 {2,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(1576)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
        5  O u0 p2 c0 {1,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(241643)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        6  O u0 p2 c0 {2,S} {16,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(81674)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,D} {5,S}
        4  C u0 p0 c0 {3,D} {11,S} {12,S}
        5  O u0 p2 c0 {3,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(26828)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {4,D} {14,S} {15,S}
        6  O u0 p2 c0 {1,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(181888)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        5  O u0 p2 c0 {1,S} {13,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='C5H9(6064)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {4,S} {5,D}
        4  C u1 p0 c0 {2,S} {3,S} {12,S}
        5  C u0 p0 c0 {3,D} {13,S} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(78997)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
        3  C u0 p0 c0 {5,S} {9,S} {10,S} {14,S}
        4  C u0 p0 c0 {1,S} {2,S} {5,D}
        5  C u0 p0 c0 {3,S} {4,D} {15,S}
        6  O u0 p2 c0 {1,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(41404)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,D} {10,S}
        4  C u0 p0 c0 {3,D} {11,S} {12,S}
        5  O u0 p2 c0 {2,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(173750)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {14,S} {15,S}
        6  O u0 p2 c0 {2,S} {16,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(245241)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
        3  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        5  C u1 p0 c0 {1,S} {15,S} {16,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {3,S} {6,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(200517)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,D} {11,S}
        4  C u0 p0 c0 {3,D} {5,S} {12,S}
        5  O u0 p2 c0 {4,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(266128)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
        2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {2,S} {4,D} {5,S}
        4  C u0 p0 c0 {1,S} {3,D} {13,S}
        5  C u1 p0 c0 {3,S} {14,S} {15,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(17084)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
        5  O u0 p2 c0 {4,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(270409)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
        2  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
        3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {2,S} {4,D} {14,S}
        6  O u0 p2 c0 {1,S} {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(271118)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
        2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
        3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {4,D} {15,S} {16,S}
        6  O u0 p2 c0 {2,S} {8,S}
        7  O u0 p2 c0 {1,S} {17,S}
        8  O u0 p2 c0 {6,S} {18,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 O u1 p2 c0 {7,S}
        18 H u0 p0 c0 {8,S}
        """),
)
            
species(
    label='S(40600)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
        2  C u0 p0 c0 {4,D} {5,S} {11,S}
        3  C u0 p0 c0 {5,S} {7,S} {12,D}
        4  C u0 p0 c0 {2,D} {13,S} {14,S}
        5  O u0 p2 c0 {2,S} {3,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {3,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {2,S}
        12 O u0 p2 c0 {3,D}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(271116)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
        2  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
        3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {2,S} {4,D} {16,S}
        6  O u0 p2 c0 {2,S} {8,S}
        7  O u0 p2 c0 {1,S} {17,S}
        8  O u0 p2 c0 {6,S} {18,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {1,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {5,S}
        17 O u1 p2 c0 {7,S}
        18 H u0 p0 c0 {8,S}
        """),
)
            
species(
    label='S(95204)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        5  O u0 p2 c0 {1,S} {14,S}
        6  O u0 p2 c0 {2,S} {13,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {6,S}
        14 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(276377)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
        5  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        6  O u0 p2 c0 {2,S} {4,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(281217)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {8,S} {9,S} {12,S}
        4  C u0 p0 c0 {1,S} {2,S} {5,D}
        5  C u0 p0 c0 {4,D} {13,S} {14,S}
        6  O u0 p2 c0 {1,S} {2,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(276397)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
        3  C u0 p0 c0 {1,S} {2,S} {7,S} {9,S}
        4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        5  C u0 p0 c0 {1,S} {11,S} {15,S} {16,S}
        6  O u0 p2 c0 {2,S} {8,S}
        7  O u0 p2 c0 {3,S} {17,S}
        8  O u0 p2 c0 {6,S} {18,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 O u1 p2 c0 {7,S}
        18 H u0 p0 c0 {8,S}
        """),
)
            
species(
    label='S(291029)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {3,S} {4,D}
        3  C u0 p0 c0 {2,S} {5,D} {9,S}
        4  C u0 p0 c0 {2,D} {12,S} {13,S}
        5  C u0 p0 c0 {3,D} {10,S} {11,S}
        6  O u0 p2 c0 {1,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {5,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(281216)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
        3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {4,D} {13,S} {14,S}
        6  O u0 p2 c0 {2,S} {3,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(296124)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
        3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {4,D} {12,S} {13,S}
        6  O u0 p2 c0 {1,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(303684)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,D} {9,S}
        3  C u0 p0 c0 {1,S} {5,D} {8,S}
        4  C u0 p0 c0 {2,D} {10,S} {11,S}
        5  C u0 p0 c0 {3,D} {12,S} {13,S}
        6  O u0 p2 c0 {1,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(307269)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
        3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {5,D} {12,S}
        5  C u0 p0 c0 {3,S} {4,D} {13,S}
        6  O u0 p2 c0 {1,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(75944)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {4,D} {10,S}
        3  C u0 p0 c0 {4,S} {5,D} {6,S}
        4  C u0 p0 c0 {2,D} {3,S} {11,S}
        5  C u0 p0 c0 {3,D} {12,S} {13,S}
        6  O u0 p2 c0 {3,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(13324)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,D} {11,S}
        4  C u0 p0 c0 {3,D} {5,S} {12,S}
        5  C u0 p0 c0 {4,S} {13,D} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 O u0 p2 c0 {5,D}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(1907)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {5,D} {10,S}
        4  C u0 p0 c0 {2,S} {11,D} {12,S}
        5  C u0 p0 c0 {3,D} {13,S} {14,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {3,S}
        11 O u0 p2 c0 {4,D}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(14137)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        5  C u0 p0 c0 {2,S} {13,D} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 O u0 p2 c0 {5,D}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(1627)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
        5  C u0 p0 c0 {1,S} {13,D} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 O u0 p2 c0 {5,D}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(13322)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,D} {10,S}
        4  C u0 p0 c0 {1,S} {11,D} {12,S}
        5  C u0 p0 c0 {3,D} {13,S} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 O u0 p2 c0 {4,D}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(1620)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
        3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        5  C u0 p0 c0 {1,S} {3,S} {14,D}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(3125)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
        2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,S} {5,D}
        4  C u0 p0 c0 {2,S} {3,S} {12,D}
        5  C u0 p0 c0 {3,D} {13,S} {14,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {1,S}
        12 O u0 p2 c0 {4,D}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(1666)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,S} {11,D}
        4  C u0 p0 c0 {3,S} {5,D} {12,S}
        5  C u0 p0 c0 {4,D} {13,S} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 O u0 p2 c0 {3,D}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(320602)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
        4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
        5  C u0 p0 c0 {3,S} {4,S} {14,D}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(291041)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
        2  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
        3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {4,D} {15,S} {16,S}
        6  O u0 p2 c0 {1,S} {8,S}
        7  O u0 p2 c0 {2,S} {17,S}
        8  O u0 p2 c0 {6,S} {18,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 O u1 p2 c0 {7,S}
        18 H u0 p0 c0 {8,S}
        """),
)
            
species(
    label='S(3124)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {2,S} {11,D}
        4  C u0 p0 c0 {1,S} {5,D} {12,S}
        5  C u0 p0 c0 {4,D} {13,S} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 O u0 p2 c0 {3,D}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(2230)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        5  C u0 p0 c0 {2,S} {3,S} {14,D}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(3126)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {5,S} {12,D}
        4  C u0 p0 c0 {2,S} {5,D} {13,S}
        5  C u0 p0 c0 {3,S} {4,D} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 O u0 p2 c0 {3,D}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(144565)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {14,D}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(345046)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
        2  C u0 p0 c0 {1,S} {4,S} {6,S} {10,S}
        3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
        4  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
        6  O u0 p2 c0 {2,S} {7,S}
        7  O u0 p2 c0 {3,S} {6,S}
        8  O u0 p2 c0 {4,S} {18,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {5,S}
        18 O u1 p2 c0 {8,S}
        """),
)
            
species(
    label='S(276390)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {10,S}
        3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
        4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
        6  O u0 p2 c0 {4,S} {7,S}
        7  O u0 p2 c0 {3,S} {6,S}
        8  O u0 p2 c0 {2,S} {18,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {5,S}
        18 O u1 p2 c0 {8,S}
        """),
)
            
species(
    label='S(4264)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {14,D}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(144566)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {4,D} {14,D}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(276398)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
        3  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {3,S} {6,S}
        8  O u0 p2 c0 {2,S} {18,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {5,S}
        18 O u1 p2 c0 {8,S}
        """),
)
            
species(
    label='S(367343)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        4  C u0 p0 c0 {1,S} {5,D} {7,S}
        5  C u0 p0 c0 {4,D} {15,S} {16,S}
        6  O u0 p2 c0 {1,S} {8,S}
        7  O u0 p2 c0 {4,S} {17,S}
        8  O u0 p2 c0 {6,S} {18,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 O u1 p2 c0 {7,S}
        18 H u0 p0 c0 {8,S}
        """),
)
            
species(
    label='S(14136)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {13,D} {14,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 O u0 p2 c0 {5,D}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(13323)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,S} {5,D}
        4  C u0 p0 c0 {3,S} {11,D} {12,S}
        5  C u0 p0 c0 {3,D} {13,S} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 O u0 p2 c0 {4,D}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(372262)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        5  C u0 p0 c0 {2,S} {11,S} {15,S} {16,S}
        6  O u0 p2 c0 {1,S} {8,S}
        7  O u0 p2 c0 {2,S} {17,S}
        8  O u0 p2 c0 {6,S} {18,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 O u1 p2 c0 {7,S}
        18 H u0 p0 c0 {8,S}
        """),
)
            
species(
    label='S(14138)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
        5  C u0 p0 c0 {4,S} {13,D} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 O u0 p2 c0 {5,D}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(377370)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {12,S}
        3  C u0 p0 c0 {1,S} {11,S} {13,S} {14,S}
        4  C u0 p0 c0 {1,S} {5,D} {7,S}
        5  C u0 p0 c0 {4,D} {15,S} {16,S}
        6  O u0 p2 c0 {1,S} {17,S}
        7  O u0 p2 c0 {4,S} {8,S}
        8  O u0 p2 c0 {7,S} {18,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 O u1 p2 c0 {6,S}
        18 H u0 p0 c0 {8,S}
        """),
)
            
species(
    label='S(383408)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {10,S}
        3  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {14,S} {15,S}
        6  O u0 p2 c0 {1,S} {16,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 O u1 p2 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 O u1 p2 c0 {6,S}
        """),
)
            
species(
    label='S(3212)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,D} {9,S}
        3  C u0 p0 c0 {1,S} {5,D} {10,S}
        4  C u0 p0 c0 {2,D} {6,S} {11,S}
        5  C u0 p0 c0 {3,D} {12,S} {13,S}
        6  O u0 p2 c0 {4,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(1921)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,D} {12,S}
        4  C u0 p0 c0 {2,S} {3,D} {11,S}
        5  C u0 p0 c0 {1,S} {13,D} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {3,S}
        13 O u0 p2 c0 {5,D}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(388569)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {11,S}
        3  C u0 p0 c0 {1,S} {10,S} {12,S} {13,S}
        4  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
        5  C u0 p0 c0 {1,S} {4,S} {16,D}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {4,S} {6,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(397988)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
        4  C u0 p0 c0 {2,S} {5,D} {13,S}
        5  C u0 p0 c0 {3,S} {4,D} {12,S}
        6  O u0 p2 c0 {1,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(397997)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
        2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {2,S} {4,S} {5,D}
        4  C u0 p0 c0 {1,S} {3,S} {13,D}
        5  C u0 p0 c0 {3,D} {14,S} {15,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 O u0 p2 c0 {4,D}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(3497)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
        2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
        3  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
        4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        5  C u0 p0 c0 {1,S} {3,S} {15,D}
        6  O u0 p2 c0 {3,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 O u0 p2 c0 {5,D}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(3216)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {3,D} {10,S}
        3  C u0 p0 c0 {2,D} {4,S} {12,S}
        4  C u0 p0 c0 {3,S} {5,D} {11,S}
        5  C u0 p0 c0 {4,D} {6,S} {13,S}
        6  O u0 p2 c0 {5,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(75912)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,D} {6,S}
        3  C u0 p0 c0 {1,S} {5,D} {9,S}
        4  C u0 p0 c0 {2,D} {12,S} {13,S}
        5  C u0 p0 c0 {3,D} {10,S} {11,S}
        6  O u0 p2 c0 {2,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {5,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(411036)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {4,S} {12,D}
        4  C u0 p0 c0 {3,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {14,S} {15,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 O u0 p2 c0 {3,D}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(342521)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
        3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
        4  C u0 p0 c0 {2,S} {5,D} {6,S}
        5  C u0 p0 c0 {3,S} {4,D} {13,S}
        6  O u0 p2 c0 {4,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(419582)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
        2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
        3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
        4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
        5  C u0 p0 c0 {1,S} {4,S} {15,D}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 O u0 p2 c0 {5,D}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(121851)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {3,D} {6,S}
        3  C u0 p0 c0 {2,D} {4,S} {11,S}
        4  C u0 p0 c0 {3,S} {5,D} {10,S}
        5  C u0 p0 c0 {4,D} {12,S} {13,S}
        6  O u0 p2 c0 {2,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(428498)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
        2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {2,S} {12,D}
        4  C u0 p0 c0 {1,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {14,S} {15,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 O u0 p2 c0 {3,D}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(436220)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
        2  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        5  C u0 p0 c0 {2,S} {3,S} {15,D}
        6  O u0 p2 c0 {2,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 O u0 p2 c0 {5,D}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(112246)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {3,D} {4,S} {6,S}
        3  C u0 p0 c0 {1,S} {2,D} {10,S}
        4  C u0 p0 c0 {2,S} {5,D} {11,S}
        5  C u0 p0 c0 {4,D} {12,S} {13,S}
        6  O u0 p2 c0 {2,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(125892)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
        3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {3,S} {5,D} {6,S}
        5  C u0 p0 c0 {1,S} {4,D} {14,S}
        6  O u0 p2 c0 {2,S} {4,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(436211)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
        2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
        3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
        4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {1,S} {4,S} {16,D}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {3,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(419581)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
        3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        5  C u0 p0 c0 {1,S} {3,S} {15,D}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 O u0 p2 c0 {5,D}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(125890)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {6,S} {14,S}
        6  O u0 p2 c0 {1,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(116900)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {5,D} {6,S}
        5  C u0 p0 c0 {1,S} {4,D} {13,S}
        6  O u0 p2 c0 {4,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(419583)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {5,S} {6,S} {8,S}
        2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
        3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {1,S} {2,S} {16,D}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {3,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(342520)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {5,D} {6,S}
        5  C u0 p0 c0 {4,D} {13,S} {14,S}
        6  O u0 p2 c0 {3,S} {4,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(419591)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
        2  C u0 p0 c0 {4,S} {5,S} {7,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {1,S} {2,S} {16,D}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {2,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(116899)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {5,D} {6,S}
        5  C u0 p0 c0 {2,S} {4,D} {13,S}
        6  O u0 p2 c0 {4,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(454610)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
        2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {1,S} {5,D} {13,S}
        4  C u0 p0 c0 {2,S} {5,S} {14,D}
        5  C u0 p0 c0 {3,D} {4,S} {15,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {3,S}
        14 O u0 p2 c0 {4,D}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(481170)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
        2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {5,S} {9,S} {12,S}
        4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
        5  C u0 p0 c0 {2,S} {3,S} {15,D}
        6  O u0 p2 c0 {4,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 O u0 p2 c0 {5,D}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(1916)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {2,S} {5,D}
        4  C u0 p0 c0 {1,S} {11,D} {12,S}
        5  C u0 p0 c0 {3,D} {13,S} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 O u0 p2 c0 {4,D}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(481177)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
        2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        3  C u0 p0 c0 {5,S} {7,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {5,D} {15,S}
        5  C u0 p0 c0 {3,S} {4,D} {14,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {3,S} {6,S}
        8  O u0 p2 c0 {1,S} {16,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {8,S}
        """),
)
            
species(
    label='S(326710)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {6,S} {14,S}
        6  O u0 p2 c0 {3,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(326711)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {3,S} {5,D}
        5  C u0 p0 c0 {4,D} {6,S} {13,S}
        6  O u0 p2 c0 {5,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(17538)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
        2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {1,S} {5,D} {13,S}
        4  C u0 p0 c0 {2,S} {7,S} {14,D}
        5  C u0 p0 c0 {3,D} {15,S} {16,S}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {4,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {3,S}
        14 O u0 p2 c0 {4,D}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(40450)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
        2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {2,S} {7,S} {16,D}
        6  O u0 p2 c0 {3,S} {7,S}
        7  O u0 p2 c0 {5,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(108730)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {5,D} {6,S}
        5  C u0 p0 c0 {4,D} {13,S} {14,S}
        6  O u0 p2 c0 {1,S} {4,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(127874)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {5,D} {12,S}
        5  C u0 p0 c0 {2,S} {4,D} {13,S}
        6  O u0 p2 c0 {1,S} {14,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(45116)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
        2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {1,S} {2,S} {5,D}
        4  C u0 p0 c0 {1,S} {6,S} {13,D}
        5  C u0 p0 c0 {3,D} {14,S} {15,S}
        6  O u0 p2 c0 {4,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 O u0 p2 c0 {4,D}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(121850)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {3,S} {4,D}
        3  C u0 p0 c0 {2,S} {5,D} {10,S}
        4  C u0 p0 c0 {2,D} {6,S} {11,S}
        5  C u0 p0 c0 {3,D} {12,S} {13,S}
        6  O u0 p2 c0 {4,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(48717)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {2,S} {7,S} {16,D}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {5,S} {6,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(53925)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {8,S} {9,S} {13,S}
        2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {1,S} {5,D} {6,S}
        4  C u0 p0 c0 {2,S} {7,S} {14,D}
        5  C u0 p0 c0 {3,D} {15,S} {16,S}
        6  O u0 p2 c0 {3,S} {7,S}
        7  O u0 p2 c0 {4,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {1,S}
        14 O u0 p2 c0 {4,D}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(125891)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
        3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {4,D} {6,S} {14,S}
        6  O u0 p2 c0 {2,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(40452)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
        2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
        3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {3,S} {7,S} {16,D}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {5,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(116901)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
        3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {2,S} {4,D} {6,S}
        6  O u0 p2 c0 {5,S} {14,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(543538)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {5,D} {12,S}
        4  C u0 p0 c0 {2,S} {6,S} {13,D}
        5  C u0 p0 c0 {3,D} {14,S} {15,S}
        6  O u0 p2 c0 {4,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 O u0 p2 c0 {4,D}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(26580)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        4  C u0 p0 c0 {2,S} {12,D} {13,S}
        5  O u0 p2 c0 {1,S} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 O u0 p2 c0 {4,D}
        13 H u0 p0 c0 {4,S}
        14 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(127875)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
        3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {5,D} {13,S}
        5  C u0 p0 c0 {2,S} {4,D} {12,S}
        6  O u0 p2 c0 {2,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(551138)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
        2  C u0 p0 c0 {1,S} {3,S} {5,S} {9,S}
        3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        5  C u0 p0 c0 {2,S} {6,S} {15,D}
        6  O u0 p2 c0 {5,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 O u0 p2 c0 {5,D}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(112244)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {5,D} {11,S}
        5  C u0 p0 c0 {4,D} {12,S} {13,S}
        6  O u0 p2 c0 {1,S} {14,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(309528)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {3,D} {9,S}
        3  C u0 p0 c0 {2,D} {4,S} {11,S}
        4  C u0 p0 c0 {3,S} {5,D} {10,S}
        5  C u0 p0 c0 {4,D} {12,S} {13,S}
        6  O u0 p2 c0 {1,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(503490)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
        4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
        5  C u0 p0 c0 {3,S} {7,S} {16,D}
        6  O u0 p2 c0 {4,S} {7,S}
        7  O u0 p2 c0 {5,S} {6,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(75937)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {3,S} {4,D}
        3  C u0 p0 c0 {2,S} {5,D} {6,S}
        4  C u0 p0 c0 {2,D} {10,S} {11,S}
        5  C u0 p0 c0 {3,D} {12,S} {13,S}
        6  O u0 p2 c0 {3,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(45115)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {5,D} {12,S}
        4  C u0 p0 c0 {1,S} {6,S} {13,D}
        5  C u0 p0 c0 {3,D} {14,S} {15,S}
        6  O u0 p2 c0 {4,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 O u0 p2 c0 {4,D}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(206388)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {5,D} {6,S}
        4  C u0 p0 c0 {5,D} {12,S} {13,S}
        5  C u0 p0 c0 {3,D} {4,D}
        6  O u0 p2 c0 {3,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(25579)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
        3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {7,S} {16,D}
        6  O u0 p2 c0 {2,S} {7,S}
        7  O u0 p2 c0 {5,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(569370)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
        3  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {5,D} {14,S}
        5  C u0 p0 c0 {3,S} {4,D} {13,S}
        6  O u0 p2 c0 {2,S} {3,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(28998)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
        3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {3,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 O u1 p2 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(40451)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
        2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
        3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {1,S} {7,S} {16,D}
        6  O u0 p2 c0 {3,S} {7,S}
        7  O u0 p2 c0 {5,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(551132)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
        4  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {6,S} {15,D}
        6  O u0 p2 c0 {5,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 O u0 p2 c0 {5,D}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(569376)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {5,D} {14,S}
        5  C u0 p0 c0 {2,S} {4,D} {13,S}
        6  O u0 p2 c0 {1,S} {2,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(45117)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
        2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {1,S} {4,D} {13,S}
        4  C u0 p0 c0 {2,S} {3,D} {14,S}
        5  C u0 p0 c0 {1,S} {6,S} {15,D}
        6  O u0 p2 c0 {5,S} {7,S}
        7  O u0 p2 c0 {6,S} {16,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 O u0 p2 c0 {5,D}
        16 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(3214)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {3,S} {5,D}
        3  C u0 p0 c0 {2,S} {4,D} {10,S}
        4  C u0 p0 c0 {3,D} {6,S} {11,S}
        5  C u0 p0 c0 {2,D} {12,S} {13,S}
        6  O u0 p2 c0 {4,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(125889)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {6,S} {14,S}
        6  O u0 p2 c0 {2,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(48718)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {3,S} {7,S} {16,D}
        6  O u0 p2 c0 {1,S} {7,S}
        7  O u0 p2 c0 {5,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(24700)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
        2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {5,D} {14,S}
        4  C u0 p0 c0 {2,S} {6,S} {15,D}
        5  C u0 p0 c0 {3,D} {7,S} {16,S}
        6  O u0 p2 c0 {4,S} {7,S}
        7  O u0 p2 c0 {5,S} {6,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {1,S}
        13 H u0 p0 c0 {1,S}
        14 H u0 p0 c0 {3,S}
        15 O u0 p2 c0 {4,D}
        16 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(121848)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {5,D} {11,S}
        5  C u0 p0 c0 {4,D} {12,S} {13,S}
        6  O u0 p2 c0 {2,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(2401)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {1,S} {6,S} {13,D}
        4  C u0 p0 c0 {5,D} {7,S} {14,S}
        5  C u0 p0 c0 {4,D} {15,S} {16,S}
        6  O u0 p2 c0 {3,S} {7,S}
        7  O u0 p2 c0 {4,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 O u0 p2 c0 {3,D}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(419577)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
        4  C u0 p0 c0 {2,S} {3,S} {5,D}
        5  C u0 p0 c0 {4,D} {12,S} {13,S}
        6  O u0 p2 c0 {1,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(595181)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
        2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
        3  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
        4  C u1 p0 c0 {1,S} {3,S} {17,S}
        5  C u0 p0 c0 {7,S} {8,S} {18,D}
        6  O u0 p2 c0 {2,S} {7,S}
        7  O u0 p2 c0 {5,S} {6,S}
        8  O u0 p2 c0 {5,S} {9,S}
        9  O u0 p2 c0 {8,S} {19,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {3,S}
        17 H u0 p0 c0 {4,S}
        18 O u0 p2 c0 {5,D}
        19 H u0 p0 c0 {9,S}
        """),
)
            
species(
    label='S(1918)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {4,D} {6,S}
        3  C u0 p0 c0 {5,D} {6,S} {10,S}
        4  C u0 p0 c0 {2,D} {13,S} {14,S}
        5  C u0 p0 c0 {3,D} {11,S} {12,S}
        6  O u0 p2 c0 {2,S} {3,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(29433)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
        2  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {1,S} {5,D} {13,S}
        4  C u0 p0 c0 {1,S} {7,S} {14,D}
        5  C u0 p0 c0 {3,D} {15,S} {16,S}
        6  O u0 p2 c0 {2,S} {7,S}
        7  O u0 p2 c0 {4,S} {6,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {3,S}
        14 O u0 p2 c0 {4,D}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='CHO4(267)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {4,S} {5,D}
        2 O u0 p2 c0 {1,S} {3,S}
        3 O u0 p2 c0 {2,S} {6,S}
        4 O u1 p2 c0 {1,S}
        5 O u0 p2 c0 {1,D}
        6 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='S(108731)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
        3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {1,S} {5,D} {6,S}
        5  C u0 p0 c0 {3,S} {4,D} {14,S}
        6  O u0 p2 c0 {2,S} {4,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(119085)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {11,S}
        2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
        3  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
        4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
        5  C u0 p0 c0 {8,S} {9,S} {19,D}
        6  O u0 p2 c0 {3,S} {8,S}
        7  O u0 p2 c0 {1,S} {20,S}
        8  O u0 p2 c0 {5,S} {6,S}
        9  O u0 p2 c0 {5,S} {10,S}
        10 O u0 p2 c0 {9,S} {21,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {4,S}
        19 O u0 p2 c0 {5,D}
        20 O u1 p2 c0 {7,S}
        21 H u0 p0 c0 {10,S}
        """),
)
            
species(
    label='S(4826)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
        3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {3,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(151260)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        5  C u0 p0 c0 {1,S} {2,S} {14,D}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(312)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        4  O u0 p2 c0 {2,S} {12,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 O u1 p2 c0 {4,S}
        """),
)
            
species(
    label='S(11637)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,D} {11,S}
        4  C u0 p0 c0 {3,D} {12,S} {13,S}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {5,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(241543)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {5,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        5  O u0 p2 c0 {2,S} {6,S}
        6  O u0 p2 c0 {5,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(1662)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,D} {11,S}
        4  C u0 p0 c0 {3,D} {12,S} {13,S}
        5  O u0 p2 c0 {2,S} {6,S}
        6  O u0 p2 c0 {5,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(226957)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
        2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {4,D} {13,S}
        4  C u0 p0 c0 {2,S} {3,D} {12,S}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {5,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(1601)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
        4  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {5,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(11649)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {4,D} {5,S}
        4  C u0 p0 c0 {3,D} {12,S} {13,S}
        5  O u0 p2 c0 {3,S} {6,S}
        6  O u0 p2 c0 {5,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(1027)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,S} {10,D}
        4  C u1 p0 c0 {3,S} {11,S} {12,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 O u0 p2 c0 {3,D}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(13299)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {2,S} {13,D}
        5  O u0 p2 c0 {2,S} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 O u0 p2 c0 {4,D}
        14 O u1 p2 c0 {5,S}
        """),
)
            
species(
    label='S(151261)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
        3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        5  C u0 p0 c0 {1,S} {2,S} {14,D}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(14106)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2 C u0 p0 c0 {1,S} {4,S} {7,D}
        3 O u0 p2 c0 {1,S} {4,S}
        4 O u0 p2 c0 {2,S} {3,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 O u0 p2 c0 {2,D}
        """),
)
            
species(
    label='S(173)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {6,S} {7,D}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 O u1 p2 c0 {2,S}
        7 O u0 p2 c0 {2,D}
        """),
)
            
species(
    label='S(1913)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,D} {9,S}
        3  C u0 p0 c0 {5,D} {6,S} {10,S}
        4  C u0 p0 c0 {2,D} {13,S} {14,S}
        5  C u0 p0 c0 {3,D} {11,S} {12,S}
        6  O u0 p2 c0 {1,S} {3,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(16894)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
        3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
        4  C u1 p0 c0 {1,S} {12,S} {13,S}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {3,S} {5,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(452)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {6,S} {7,D}
        3 O u1 p2 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 O u1 p2 c0 {2,S}
        7 O u0 p2 c0 {2,D}
        """),
)
            
species(
    label='S(62560)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {5,D}
        2 O u0 p2 c0 {1,S} {4,S}
        3 O u0 p2 c0 {1,S} {6,S}
        4 O u0 p2 c0 {2,S} {7,S}
        5 O u0 p2 c0 {1,D}
        6 O u1 p2 c0 {3,S}
        7 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(181904)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
        2  C u1 p0 c0 {1,S} {3,S} {9,S}
        3  C u0 p0 c0 {2,S} {4,D} {10,S}
        4  C u0 p0 c0 {3,D} {11,S} {12,S}
        5  O u0 p2 c0 {1,S} {6,S}
        6  O u0 p2 c0 {5,S} {13,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(312838)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {5,D} {12,S}
        4  C u0 p0 c0 {5,D} {6,S} {13,S}
        5  C u0 p0 c0 {3,D} {4,D}
        6  O u0 p2 c0 {4,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(276396)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
        2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,D} {11,S}
        4  C u0 p0 c0 {3,D} {12,S} {13,S}
        5  O u0 p2 c0 {2,S} {7,S}
        6  O u0 p2 c0 {1,S} {14,S}
        7  O u0 p2 c0 {5,S} {15,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 O u1 p2 c0 {6,S}
        15 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(121849)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {5,D} {12,S}
        5  C u0 p0 c0 {4,D} {6,S} {13,S}
        6  O u0 p2 c0 {5,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(112234)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {3,S} {4,D} {6,S}
        3  C u0 p0 c0 {2,S} {5,D} {10,S}
        4  C u0 p0 c0 {2,D} {13,S} {14,S}
        5  C u0 p0 c0 {3,D} {11,S} {12,S}
        6  O u0 p2 c0 {1,S} {2,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(281196)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
        2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {4,D} {12,S}
        4  C u0 p0 c0 {2,S} {3,D} {13,S}
        5  O u0 p2 c0 {1,S} {7,S}
        6  O u0 p2 c0 {2,S} {14,S}
        7  O u0 p2 c0 {5,S} {15,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 O u1 p2 c0 {6,S}
        15 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(108729)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {5,D} {6,S}
        5  C u0 p0 c0 {4,D} {13,S} {14,S}
        6  O u0 p2 c0 {2,S} {4,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(276376)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,D} {10,S}
        4  C u0 p0 c0 {2,S} {3,D} {11,S}
        5  O u0 p2 c0 {1,S} {2,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(2391)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
        3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
        5  O u0 p2 c0 {1,S} {7,S}
        6  O u0 p2 c0 {2,S} {14,S}
        7  O u0 p2 c0 {5,S} {15,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 O u1 p2 c0 {6,S}
        15 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='CCCOO(983)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  O u0 p2 c0 {2,S} {5,S}
        5  O u0 p2 c0 {4,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(1923)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {3,D} {10,S}
        3  C u0 p0 c0 {2,D} {6,S} {12,S}
        4  C u0 p0 c0 {5,D} {6,S} {11,S}
        5  C u0 p0 c0 {4,D} {13,S} {14,S}
        6  O u0 p2 c0 {3,S} {4,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(121840)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {3,S} {4,D} {11,S}
        3  C u0 p0 c0 {2,S} {5,D} {10,S}
        4  C u0 p0 c0 {2,D} {6,S} {12,S}
        5  C u0 p0 c0 {3,D} {13,S} {14,S}
        6  O u0 p2 c0 {1,S} {4,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='C3H7O(145)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
        4  H u0 p0 c0 {1,S}
        5  H u0 p0 c0 {1,S}
        6  H u0 p0 c0 {3,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 O u1 p2 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        """),
)
            
species(
    label='S(62567)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {3,S} {6,D}
        2 O u0 p2 c0 {1,S} {4,S}
        3 O u0 p2 c0 {1,S} {5,S}
        4 O u0 p2 c0 {2,S} {7,S}
        5 O u0 p2 c0 {3,S} {8,S}
        6 O u0 p2 c0 {1,D}
        7 H u0 p0 c0 {4,S}
        8 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(127877)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {3,S} {5,D}
        5  C u0 p0 c0 {1,S} {4,D} {13,S}
        6  O u0 p2 c0 {1,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(69359)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {8,S} {14,S}
        2  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
        3  C u0 p0 c0 {1,S} {20,S} {21,S} {22,S}
        4  C u0 p0 c0 {5,S} {9,S} {15,S} {16,S}
        5  C u0 p0 c0 {4,S} {10,S} {23,D}
        6  C u0 p0 c0 {11,S} {12,S} {24,D}
        7  C u0 p0 c0 {13,S} {25,D} {26,S}
        8  O u0 p2 c0 {1,S} {12,S}
        9  O u0 p2 c0 {4,S} {11,S}
        10 O u0 p2 c0 {5,S} {13,S}
        11 O u0 p2 c0 {6,S} {9,S}
        12 O u0 p2 c0 {6,S} {8,S}
        13 O u0 p2 c0 {7,S} {10,S}
        14 O u1 p2 c0 {1,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {2,S}
        18 H u0 p0 c0 {2,S}
        19 H u0 p0 c0 {2,S}
        20 H u0 p0 c0 {3,S}
        21 H u0 p0 c0 {3,S}
        22 H u0 p0 c0 {3,S}
        23 O u0 p2 c0 {5,D}
        24 O u0 p2 c0 {6,D}
        25 O u0 p2 c0 {7,D}
        26 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(111201)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
        2  C u0 p0 c0 {4,S} {8,S} {15,S} {16,S}
        3  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
        4  C u0 p0 c0 {2,S} {9,S} {20,D}
        5  C u0 p0 c0 {10,S} {11,S} {21,D}
        6  C u0 p0 c0 {12,S} {22,D} {23,S}
        7  O u0 p2 c0 {1,S} {11,S}
        8  O u0 p2 c0 {2,S} {10,S}
        9  O u0 p2 c0 {4,S} {12,S}
        10 O u0 p2 c0 {5,S} {8,S}
        11 O u0 p2 c0 {5,S} {7,S}
        12 O u0 p2 c0 {6,S} {9,S}
        13 O u1 p2 c0 {1,S}
        14 H u0 p0 c0 {1,S}
        15 H u0 p0 c0 {2,S}
        16 H u0 p0 c0 {2,S}
        17 H u0 p0 c0 {3,S}
        18 H u0 p0 c0 {3,S}
        19 H u0 p0 c0 {3,S}
        20 O u0 p2 c0 {4,D}
        21 O u0 p2 c0 {5,D}
        22 O u0 p2 c0 {6,D}
        23 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(62586)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {2,S} {4,D}
        4  C u0 p0 c0 {3,D} {5,S} {12,S}
        5  C u0 p0 c0 {4,S} {13,D} {14,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {4,S}
        13 O u0 p2 c0 {5,D}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(782147)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
        2  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
        3  C u0 p0 c0 {1,S} {8,S} {18,D}
        4  C u0 p0 c0 {2,S} {9,S} {19,D}
        5  C u0 p0 c0 {10,S} {11,S} {20,D}
        6  C u0 p0 c0 {12,S} {21,S} {22,D}
        7  O u0 p2 c0 {1,S} {10,S}
        8  O u0 p2 c0 {3,S} {12,S}
        9  O u0 p2 c0 {4,S} {11,S}
        10 O u0 p2 c0 {5,S} {7,S}
        11 O u0 p2 c0 {5,S} {9,S}
        12 O u0 p2 c0 {6,S} {8,S}
        13 H u0 p0 c0 {1,S}
        14 H u0 p0 c0 {1,S}
        15 H u0 p0 c0 {2,S}
        16 H u0 p0 c0 {2,S}
        17 H u0 p0 c0 {2,S}
        18 O u0 p2 c0 {3,D}
        19 O u0 p2 c0 {4,D}
        20 O u0 p2 c0 {5,D}
        21 H u0 p0 c0 {6,S}
        22 O u0 p2 c0 {6,D}
        """),
)
            
species(
    label='S(296126)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {5,D} {12,S}
        5  C u0 p0 c0 {2,S} {4,D} {13,S}
        6  O u0 p2 c0 {3,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(142581)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
        2  C u0 p0 c0 {1,S} {7,S} {14,D}
        3  C u0 p0 c0 {8,S} {9,S} {15,D}
        4  C u0 p0 c0 {10,S} {16,S} {17,D}
        5  C u0 p0 c0 {11,S} {18,D} {19,S}
        6  O u0 p2 c0 {1,S} {8,S}
        7  O u0 p2 c0 {2,S} {11,S}
        8  O u0 p2 c0 {3,S} {6,S}
        9  O u0 p2 c0 {3,S} {10,S}
        10 O u0 p2 c0 {4,S} {9,S}
        11 O u0 p2 c0 {5,S} {7,S}
        12 H u0 p0 c0 {1,S}
        13 H u0 p0 c0 {1,S}
        14 O u0 p2 c0 {2,D}
        15 O u0 p2 c0 {3,D}
        16 H u0 p0 c0 {4,S}
        17 O u0 p2 c0 {4,D}
        18 O u0 p2 c0 {5,D}
        19 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(803844)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {14,S}
        2  C u0 p0 c0 {1,S} {8,S} {12,S} {15,S}
        3  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
        4  C u0 p0 c0 {1,S} {9,S} {19,D}
        5  C u0 p0 c0 {3,S} {10,S} {20,D}
        6  C u0 p0 c0 {11,S} {13,S} {21,D}
        7  O u0 p2 c0 {1,S} {11,S}
        8  O u0 p2 c0 {2,S} {9,S}
        9  O u0 p2 c0 {4,S} {8,S}
        10 O u0 p2 c0 {5,S} {13,S}
        11 O u0 p2 c0 {6,S} {7,S}
        12 O u0 p2 c0 {2,S} {22,S}
        13 O u0 p2 c0 {6,S} {10,S}
        14 H u0 p0 c0 {1,S}
        15 H u0 p0 c0 {2,S}
        16 H u0 p0 c0 {3,S}
        17 H u0 p0 c0 {3,S}
        18 H u0 p0 c0 {3,S}
        19 O u0 p2 c0 {4,D}
        20 O u0 p2 c0 {5,D}
        21 O u0 p2 c0 {6,D}
        22 H u0 p0 c0 {12,S}
        """),
)
            
species(
    label='S(143026)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {13,S}
        2  C u0 p0 c0 {1,S} {7,S} {10,S} {14,S}
        3  C u0 p0 c0 {1,S} {8,S} {15,D}
        4  C u0 p0 c0 {9,S} {11,S} {16,D}
        5  C u0 p0 c0 {12,S} {17,S} {18,D}
        6  O u0 p2 c0 {1,S} {9,S}
        7  O u0 p2 c0 {2,S} {8,S}
        8  O u0 p2 c0 {3,S} {7,S}
        9  O u0 p2 c0 {4,S} {6,S}
        10 O u0 p2 c0 {2,S} {19,S}
        11 O u0 p2 c0 {4,S} {12,S}
        12 O u0 p2 c0 {5,S} {11,S}
        13 H u0 p0 c0 {1,S}
        14 H u0 p0 c0 {2,S}
        15 O u0 p2 c0 {3,D}
        16 O u0 p2 c0 {4,D}
        17 H u0 p0 c0 {5,S}
        18 O u0 p2 c0 {5,D}
        19 H u0 p0 c0 {10,S}
        """),
)
            
species(
    label='S(127876)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {2,S} {4,D} {13,S}
        6  O u0 p2 c0 {1,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(96539)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
        2  C u0 p0 c0 {4,S} {6,S} {7,S} {11,S}
        3  C u0 p0 c0 {1,S} {4,D} {5,S}
        4  C u0 p0 c0 {2,S} {3,D} {12,S}
        5  C u0 p0 c0 {3,S} {13,D} {14,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {4,S}
        13 O u0 p2 c0 {5,D}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(8482)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
        5  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
        6  C u1 p0 c0 {4,S} {5,S} {17,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(5527)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {6,D} {13,S}
        5  C u1 p0 c0 {3,S} {14,S} {15,S}
        6  C u0 p0 c0 {4,D} {16,S} {17,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(861435)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
        3  C u0 p0 c0 {1,S} {6,S} {17,S} {18,S}
        4  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
        5  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
        6  C u0 p0 c0 {3,S} {4,S} {13,S} {14,S}
        7  O u0 p2 c0 {1,S} {19,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {6,S}
        14 H u0 p0 c0 {6,S}
        15 H u0 p0 c0 {2,S}
        16 H u0 p0 c0 {2,S}
        17 H u0 p0 c0 {3,S}
        18 H u0 p0 c0 {3,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(4370)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
        4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
        5  C u0 p0 c0 {3,S} {4,S} {14,S} {15,S}
        6  C u1 p0 c0 {1,S} {16,S} {17,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(172165)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {8,S} {10,S}
        2  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
        3  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
        4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {2,S} {6,D} {16,S}
        6  C u0 p0 c0 {5,D} {17,S} {18,S}
        7  O u0 p2 c0 {2,S} {19,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(4316)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {2,S} {5,S} {6,D}
        5  C u1 p0 c0 {4,S} {14,S} {15,S}
        6  C u0 p0 c0 {4,D} {16,S} {17,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(4823)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {2,S} {5,D} {14,S}
        5  C u0 p0 c0 {4,D} {6,S} {15,S}
        6  C u1 p0 c0 {5,S} {16,S} {17,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(171016)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
        4  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
        5  C u0 p0 c0 {3,S} {4,S} {12,S} {13,S}
        6  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
        7  O u0 p2 c0 {2,S} {19,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(166516)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {3,S} {5,D} {6,S}
        5  C u0 p0 c0 {1,S} {4,D} {14,S}
        6  O u0 p2 c0 {1,S} {4,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(172166)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,S} {10,S}
        3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
        4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
        5  C u0 p0 c0 {1,S} {4,S} {6,D}
        6  C u0 p0 c0 {5,D} {17,S} {18,S}
        7  O u0 p2 c0 {1,S} {19,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(166513)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {5,D} {13,S}
        5  C u0 p0 c0 {4,D} {6,S} {14,S}
        6  O u0 p2 c0 {1,S} {5,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(296125)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {7,S} {10,S}
        2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {2,S} {4,D} {13,S}
        6  O u0 p2 c0 {3,S} {14,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(5235)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
        4  C u0 p0 c0 {3,S} {5,S} {6,D}
        5  C u1 p0 c0 {1,S} {4,S} {15,S}
        6  C u0 p0 c0 {4,D} {16,S} {17,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(210208)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {7,S} {9,S}
        4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
        6  C u0 p0 c0 {2,S} {13,S} {17,S} {18,S}
        7  O u0 p2 c0 {3,S} {19,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {6,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(178660)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
        2  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
        5  C u0 p0 c0 {2,S} {4,S} {6,D}
        6  C u0 p0 c0 {1,S} {5,D} {18,S}
        7  O u0 p2 c0 {2,S} {19,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {2,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(172164)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
        2  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {2,S} {6,D} {16,S}
        6  C u0 p0 c0 {5,D} {17,S} {18,S}
        7  O u0 p2 c0 {2,S} {19,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(20534)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
        4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
        5  C u0 p0 c0 {1,S} {3,S} {14,D}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 O u0 p2 c0 {5,D}
        """),
)
            
species(
    label='S(372261)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {4,D} {6,S}
        4  C u0 p0 c0 {3,D} {12,S} {13,S}
        5  O u0 p2 c0 {1,S} {7,S}
        6  O u0 p2 c0 {3,S} {14,S}
        7  O u0 p2 c0 {5,S} {15,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        14 O u1 p2 c0 {6,S}
        15 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(6059)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        4  C u1 p0 c0 {1,S} {5,S} {14,S}
        5  C u0 p0 c0 {4,S} {6,D} {15,S}
        6  C u0 p0 c0 {5,D} {16,S} {17,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(62826)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
        5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        6  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
        7  O u0 p2 c0 {2,S} {19,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='C5H8(1675)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {3,D} {9,S}
        3  C u0 p0 c0 {2,D} {4,S} {11,S}
        4  C u0 p0 c0 {3,S} {5,D} {10,S}
        5  C u0 p0 c0 {4,D} {12,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(178654)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {5,S} {13,S} {14,S} {18,S}
        4  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
        5  C u0 p0 c0 {3,S} {4,S} {6,D}
        6  C u0 p0 c0 {1,S} {5,D} {7,S}
        7  O u0 p2 c0 {6,S} {19,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {3,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(166402)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
        4  C u0 p0 c0 {2,S} {5,D} {12,S}
        5  C u0 p0 c0 {3,S} {4,D} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(181949)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
        5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
        6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
        7  O u0 p2 c0 {1,S} {19,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(173875)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
        2  C u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
        3  C u0 p0 c0 {1,S} {2,S} {7,S} {10,S}
        4  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
        5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
        6  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
        7  O u0 p2 c0 {3,S} {19,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='C5H8(1673)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,D} {8,S}
        3  C u0 p0 c0 {1,S} {5,D} {9,S}
        4  C u0 p0 c0 {2,D} {10,S} {11,S}
        5  C u0 p0 c0 {3,D} {12,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(34356)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
        2  C u0 p0 c0 {7,S} {12,S} {13,S} {14,S}
        3  C u0 p0 c0 {1,S} {8,S} {15,D}
        4  C u0 p0 c0 {5,S} {9,S} {16,D}
        5  C u1 p0 c0 {4,S} {17,S} {18,S}
        6  O u0 p2 c0 {1,S} {9,S}
        7  O u0 p2 c0 {2,S} {8,S}
        8  O u0 p2 c0 {3,S} {7,S}
        9  O u0 p2 c0 {4,S} {6,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {2,S}
        15 O u0 p2 c0 {3,D}
        16 O u0 p2 c0 {4,D}
        17 H u0 p0 c0 {5,S}
        18 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(173753)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {5,D} {12,S}
        5  C u0 p0 c0 {2,S} {4,D} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(178652)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
        2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
        4  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
        5  C u0 p0 c0 {1,S} {6,D} {7,S}
        6  C u0 p0 c0 {4,S} {5,D} {18,S}
        7  O u0 p2 c0 {5,S} {19,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(351)',
    reactive=True,
    structure=adjacencyList(
        """
        1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
        2 O u0 p2 c0 {1,S} {3,S}
        3 O u0 p2 c0 {2,S} {4,S}
        4 C u1 p0 c0 {3,S} {8,D}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {1,S}
        7 H u0 p0 c0 {1,S}
        8 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='S(178651)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {5,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
        5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
        6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
        7  O u0 p2 c0 {1,S} {19,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {6,S}
        14 H u0 p0 c0 {6,S}
        15 H u0 p0 c0 {6,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {5,S}
        18 H u0 p0 c0 {5,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(195072)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {4,S} {8,S} {11,S}
        4  C u0 p0 c0 {2,S} {3,S} {5,D}
        5  C u0 p0 c0 {4,D} {12,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(36774)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {5,S} {6,S} {13,S} {14,S}
        2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
        4  C u0 p0 c0 {2,S} {8,S} {18,D}
        5  C u0 p0 c0 {1,S} {9,S} {19,D}
        6  O u0 p2 c0 {1,S} {8,S}
        7  O u0 p2 c0 {3,S} {9,S}
        8  O u0 p2 c0 {4,S} {6,S}
        9  O u0 p2 c0 {5,S} {7,S}
        10 O u0 p2 c0 {2,S} {20,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {1,S}
        14 H u0 p0 c0 {1,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {3,S}
        17 H u0 p0 c0 {3,S}
        18 O u0 p2 c0 {4,D}
        19 O u0 p2 c0 {5,D}
        20 O u1 p2 c0 {10,S}
        """),
)
            
species(
    label='S(172163)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {1,S} {6,D} {16,S}
        6  C u0 p0 c0 {5,D} {17,S} {18,S}
        7  O u0 p2 c0 {1,S} {19,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='C5H8(1674)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
        2  C u0 p0 c0 {1,S} {3,S} {4,D}
        3  C u0 p0 c0 {2,S} {5,D} {9,S}
        4  C u0 p0 c0 {2,D} {12,S} {13,S}
        5  C u0 p0 c0 {3,D} {10,S} {11,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {5,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(1005037)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
        2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
        3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
        4  C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
        5  C u0 p0 c0 {2,S} {10,S} {18,D}
        6  O u0 p2 c0 {1,S} {8,S}
        7  O u0 p2 c0 {3,S} {10,S}
        8  O u0 p2 c0 {4,S} {6,S}
        9  O u0 p2 c0 {1,S} {19,S}
        10 O u0 p2 c0 {5,S} {7,S}
        11 O u0 p2 c0 {2,S} {20,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {4,S}
        18 O u0 p2 c0 {5,D}
        19 H u0 p0 c0 {9,S}
        20 O u1 p2 c0 {11,S}
        """),
)
            
species(
    label='S(171015)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
        3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
        4  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
        5  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
        6  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
        7  O u0 p2 c0 {1,S} {19,S}
        8  H u0 p0 c0 {4,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {5,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(173752)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
        3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {3,S} {5,D}
        5  C u0 p0 c0 {2,S} {4,D} {13,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(189148)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {5,S} {9,S}
        4  C u0 p0 c0 {1,S} {13,S} {17,S} {18,S}
        5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
        6  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
        7  O u0 p2 c0 {1,S} {19,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {5,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {6,S}
        15 H u0 p0 c0 {6,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {4,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='C5H8(1206)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
        3  C u0 p0 c0 {1,S} {5,D} {11,S}
        4  C u0 p0 c0 {5,D} {12,S} {13,S}
        5  C u0 p0 c0 {3,D} {4,D}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {4,S}
        """),
)
            
species(
    label='S(1023087)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
        2  C u0 p0 c0 {6,S} {12,S} {13,S} {17,S}
        3  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
        4  C u0 p0 c0 {1,S} {8,S} {18,D}
        5  C u0 p0 c0 {1,S} {9,S} {19,D}
        6  O u0 p2 c0 {2,S} {9,S}
        7  O u0 p2 c0 {3,S} {8,S}
        8  O u0 p2 c0 {4,S} {7,S}
        9  O u0 p2 c0 {5,S} {6,S}
        10 O u0 p2 c0 {1,S} {20,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {3,S}
        17 H u0 p0 c0 {2,S}
        18 O u0 p2 c0 {4,D}
        19 O u0 p2 c0 {5,D}
        20 O u1 p2 c0 {10,S}
        """),
)
            
species(
    label='S(1037515)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {5,S} {8,S} {14,S}
        2  C u0 p0 c0 {9,S} {15,S} {16,S} {20,S}
        3  C u0 p0 c0 {10,S} {17,S} {18,S} {19,S}
        4  C u0 p0 c0 {1,S} {11,S} {21,D}
        5  C u0 p0 c0 {1,S} {12,S} {22,D}
        6  C u0 p0 c0 {7,S} {13,S} {23,D}
        7  C u1 p0 c0 {6,S} {24,S} {25,S}
        8  O u0 p2 c0 {1,S} {13,S}
        9  O u0 p2 c0 {2,S} {12,S}
        10 O u0 p2 c0 {3,S} {11,S}
        11 O u0 p2 c0 {4,S} {10,S}
        12 O u0 p2 c0 {5,S} {9,S}
        13 O u0 p2 c0 {6,S} {8,S}
        14 H u0 p0 c0 {1,S}
        15 H u0 p0 c0 {2,S}
        16 H u0 p0 c0 {2,S}
        17 H u0 p0 c0 {3,S}
        18 H u0 p0 c0 {3,S}
        19 H u0 p0 c0 {3,S}
        20 H u0 p0 c0 {2,S}
        21 O u0 p2 c0 {4,D}
        22 O u0 p2 c0 {5,D}
        23 O u0 p2 c0 {6,D}
        24 H u0 p0 c0 {7,S}
        25 H u0 p0 c0 {7,S}
        """),
)
            
species(
    label='S(181951)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        4  C u0 p0 c0 {1,S} {5,D} {11,S}
        5  C u0 p0 c0 {4,D} {12,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(173873)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
        3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
        4  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        6  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
        7  O u0 p2 c0 {1,S} {19,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {5,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(89694)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
        2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
        5  C u0 p0 c0 {2,S} {6,D} {16,S}
        6  C u0 p0 c0 {5,D} {17,S} {18,S}
        7  O u0 p2 c0 {1,S} {19,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {4,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(1047469)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
        2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
        3  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
        4  C u0 p0 c0 {1,S} {9,S} {17,D}
        5  C u0 p0 c0 {2,S} {8,S} {16,D}
        6  O u0 p2 c0 {1,S} {8,S}
        7  O u0 p2 c0 {3,S} {9,S}
        8  O u0 p2 c0 {5,S} {6,S}
        9  O u0 p2 c0 {4,S} {7,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 O u0 p2 c0 {5,D}
        17 O u0 p2 c0 {4,D}
        """),
)
            
species(
    label='C5H8(1204)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {2,S} {5,T}
        5  C u0 p0 c0 {4,T} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(189053)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
        3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {2,S} {5,D}
        5  C u0 p0 c0 {4,D} {12,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(195199)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
        2  C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
        4  C u0 p0 c0 {1,S} {2,S} {9,S} {12,S}
        5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
        6  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
        7  O u0 p2 c0 {1,S} {19,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {6,S}
        14 H u0 p0 c0 {6,S}
        15 H u0 p0 c0 {6,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {5,S}
        18 H u0 p0 c0 {5,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(1045687)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {5,S} {6,S} {8,S} {15,S}
        2  C u0 p0 c0 {7,S} {14,S} {16,S} {17,S}
        3  C u0 p0 c0 {9,S} {18,S} {19,S} {23,S}
        4  C u0 p0 c0 {10,S} {20,S} {21,S} {22,S}
        5  C u0 p0 c0 {1,S} {11,S} {25,D}
        6  C u0 p0 c0 {1,S} {12,S} {26,D}
        7  C u0 p0 c0 {2,S} {13,S} {24,D}
        8  O u0 p2 c0 {1,S} {13,S}
        9  O u0 p2 c0 {3,S} {12,S}
        10 O u0 p2 c0 {4,S} {11,S}
        11 O u0 p2 c0 {5,S} {10,S}
        12 O u0 p2 c0 {6,S} {9,S}
        13 O u0 p2 c0 {7,S} {8,S}
        14 O u0 p2 c0 {2,S} {27,S}
        15 H u0 p0 c0 {1,S}
        16 H u0 p0 c0 {2,S}
        17 H u0 p0 c0 {2,S}
        18 H u0 p0 c0 {3,S}
        19 H u0 p0 c0 {3,S}
        20 H u0 p0 c0 {4,S}
        21 H u0 p0 c0 {4,S}
        22 H u0 p0 c0 {4,S}
        23 H u0 p0 c0 {3,S}
        24 O u0 p2 c0 {7,D}
        25 O u0 p2 c0 {5,D}
        26 O u0 p2 c0 {6,D}
        27 O u1 p2 c0 {14,S}
        """),
)
            
species(
    label='S(184422)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
        5  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(1081661)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {8,S} {12,S}
        2  C u0 p0 c0 {1,S} {6,S} {9,S} {16,S}
        3  C u0 p0 c0 {1,S} {7,S} {15,S} {17,S}
        4  C u0 p0 c0 {11,S} {18,S} {19,S} {23,S}
        5  C u0 p0 c0 {10,S} {20,S} {21,S} {22,S}
        6  C u0 p0 c0 {2,S} {13,S} {25,D}
        7  C u0 p0 c0 {3,S} {14,S} {24,D}
        8  O u0 p2 c0 {1,S} {10,S}
        9  O u0 p2 c0 {2,S} {14,S}
        10 O u0 p2 c0 {5,S} {8,S}
        11 O u0 p2 c0 {4,S} {13,S}
        12 O u0 p2 c0 {1,S} {26,S}
        13 O u0 p2 c0 {6,S} {11,S}
        14 O u0 p2 c0 {7,S} {9,S}
        15 O u0 p2 c0 {3,S} {27,S}
        16 H u0 p0 c0 {2,S}
        17 H u0 p0 c0 {3,S}
        18 H u0 p0 c0 {4,S}
        19 H u0 p0 c0 {4,S}
        20 H u0 p0 c0 {5,S}
        21 H u0 p0 c0 {5,S}
        22 H u0 p0 c0 {5,S}
        23 H u0 p0 c0 {4,S}
        24 O u0 p2 c0 {7,D}
        25 O u0 p2 c0 {6,D}
        26 H u0 p0 c0 {12,S}
        27 O u1 p2 c0 {15,S}
        """),
)
            
species(
    label='S(192310)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {11,S}
        3  C u0 p0 c0 {1,S} {10,S} {12,S} {13,S}
        4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
        5  C u0 p0 c0 {1,S} {6,D} {17,S}
        6  C u0 p0 c0 {4,S} {5,D} {18,S}
        7  O u0 p2 c0 {1,S} {19,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {5,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(192311)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
        3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {5,T}
        5  C u0 p0 c0 {4,T} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(192309)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {8,S} {9,S} {11,S}
        3  C u0 p0 c0 {1,S} {10,S} {12,S} {13,S}
        4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
        5  C u0 p0 c0 {1,S} {4,S} {6,D}
        6  C u0 p0 c0 {5,D} {17,S} {18,S}
        7  O u0 p2 c0 {1,S} {19,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {4,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(1039186)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {5,S} {6,S} {14,S} {15,S}
        2  C u0 p0 c0 {7,S} {8,S} {16,S} {17,S}
        3  C u0 p0 c0 {9,S} {18,S} {19,S} {20,S}
        4  C u0 p0 c0 {10,S} {21,S} {22,S} {23,S}
        5  C u0 p0 c0 {1,S} {11,S} {24,D}
        6  C u0 p0 c0 {1,S} {12,S} {25,D}
        7  C u0 p0 c0 {2,S} {13,S} {26,D}
        8  O u0 p2 c0 {2,S} {11,S}
        9  O u0 p2 c0 {3,S} {12,S}
        10 O u0 p2 c0 {4,S} {13,S}
        11 O u0 p2 c0 {5,S} {8,S}
        12 O u0 p2 c0 {6,S} {9,S}
        13 O u0 p2 c0 {7,S} {10,S}
        14 O u0 p2 c0 {1,S} {27,S}
        15 H u0 p0 c0 {1,S}
        16 H u0 p0 c0 {2,S}
        17 H u0 p0 c0 {2,S}
        18 H u0 p0 c0 {3,S}
        19 H u0 p0 c0 {3,S}
        20 H u0 p0 c0 {3,S}
        21 H u0 p0 c0 {4,S}
        22 H u0 p0 c0 {4,S}
        23 H u0 p0 c0 {4,S}
        24 O u0 p2 c0 {5,D}
        25 O u0 p2 c0 {6,D}
        26 O u0 p2 c0 {7,D}
        27 O u1 p2 c0 {14,S}
        """),
)
            
species(
    label='S(1112675)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {6,S} {7,S} {12,S}
        2  C u0 p0 c0 {1,S} {3,S} {8,S} {13,S}
        3  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
        4  C u0 p0 c0 {11,S} {18,S} {19,S} {20,S}
        5  C u0 p0 c0 {10,S} {21,S} {22,S} {23,S}
        6  C u0 p0 c0 {1,S} {14,S} {24,D}
        7  C u0 p0 c0 {1,S} {15,S} {25,D}
        8  O u0 p2 c0 {2,S} {10,S}
        9  O u0 p2 c0 {3,S} {14,S}
        10 O u0 p2 c0 {5,S} {8,S}
        11 O u0 p2 c0 {4,S} {15,S}
        12 O u0 p2 c0 {1,S} {27,S}
        13 O u0 p2 c0 {2,S} {26,S}
        14 O u0 p2 c0 {6,S} {9,S}
        15 O u0 p2 c0 {7,S} {11,S}
        16 H u0 p0 c0 {3,S}
        17 H u0 p0 c0 {3,S}
        18 H u0 p0 c0 {4,S}
        19 H u0 p0 c0 {4,S}
        20 H u0 p0 c0 {4,S}
        21 H u0 p0 c0 {5,S}
        22 H u0 p0 c0 {5,S}
        23 H u0 p0 c0 {5,S}
        24 O u0 p2 c0 {6,D}
        25 O u0 p2 c0 {7,D}
        26 H u0 p0 c0 {13,S}
        27 O u1 p2 c0 {12,S}
        """),
)
            
species(
    label='S(186896)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
        2  C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {5,S} {8,S}
        4  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        5  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {2,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(189147)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
        3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
        4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
        6  C u0 p0 c0 {2,S} {13,S} {17,S} {18,S}
        7  O u0 p2 c0 {2,S} {19,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {6,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        18 H u0 p0 c0 {6,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(189149)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
        2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
        3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
        5  C u0 p0 c0 {1,S} {15,S} {17,S} {18,S}
        6  C u0 p0 c0 {4,S} {13,S} {14,S} {16,S}
        7  O u0 p2 c0 {1,S} {19,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {4,S}
        12 H u0 p0 c0 {4,S}
        13 H u0 p0 c0 {6,S}
        14 H u0 p0 c0 {6,S}
        15 H u0 p0 c0 {5,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {5,S}
        18 H u0 p0 c0 {5,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(6065)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
        2  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
        3  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
        4  C u1 p0 c0 {1,S} {2,S} {5,S}
        5  C u0 p0 c0 {3,S} {4,S} {6,D}
        6  C u0 p0 c0 {5,D} {16,S} {17,S}
        7  H u0 p0 c0 {3,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {3,S}
        10 H u0 p0 c0 {1,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {1,S}
        13 H u0 p0 c0 {2,S}
        14 H u0 p0 c0 {2,S}
        15 H u0 p0 c0 {2,S}
        16 H u0 p0 c0 {6,S}
        17 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(1129665)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {5,S} {6,S} {7,S} {12,S}
        2  C u0 p0 c0 {8,S} {15,S} {16,S} {23,S}
        3  C u0 p0 c0 {10,S} {17,S} {18,S} {19,S}
        4  C u0 p0 c0 {9,S} {20,S} {21,S} {22,S}
        5  C u0 p0 c0 {1,S} {11,S} {24,D}
        6  C u0 p0 c0 {1,S} {13,S} {25,D}
        7  C u0 p0 c0 {1,S} {14,S} {26,D}
        8  O u0 p2 c0 {2,S} {13,S}
        9  O u0 p2 c0 {4,S} {11,S}
        10 O u0 p2 c0 {3,S} {14,S}
        11 O u0 p2 c0 {5,S} {9,S}
        12 O u0 p2 c0 {1,S} {27,S}
        13 O u0 p2 c0 {6,S} {8,S}
        14 O u0 p2 c0 {7,S} {10,S}
        15 H u0 p0 c0 {2,S}
        16 H u0 p0 c0 {2,S}
        17 H u0 p0 c0 {3,S}
        18 H u0 p0 c0 {3,S}
        19 H u0 p0 c0 {3,S}
        20 H u0 p0 c0 {4,S}
        21 H u0 p0 c0 {4,S}
        22 H u0 p0 c0 {4,S}
        23 H u0 p0 c0 {2,S}
        24 O u0 p2 c0 {5,D}
        25 O u0 p2 c0 {6,D}
        26 O u0 p2 c0 {7,D}
        27 O u1 p2 c0 {12,S}
        """),
)
            
species(
    label='S(186895)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2  C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
        3  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
        4  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
        5  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
        6  H u0 p0 c0 {2,S}
        7  H u0 p0 c0 {3,S}
        8  H u0 p0 c0 {3,S}
        9  H u0 p0 c0 {4,S}
        10 H u0 p0 c0 {4,S}
        11 H u0 p0 c0 {5,S}
        12 H u0 p0 c0 {5,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(200681)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
        2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {5,S} {13,S} {14,S} {18,S}
        4  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
        5  C u0 p0 c0 {1,S} {3,S} {6,D}
        6  C u0 p0 c0 {4,S} {5,D} {7,S}
        7  O u0 p2 c0 {6,S} {19,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {4,S}
        16 H u0 p0 c0 {4,S}
        17 H u0 p0 c0 {4,S}
        18 H u0 p0 c0 {3,S}
        19 O u1 p2 c0 {7,S}
        """),
)
            
species(
    label='S(181890)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
        2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
        3  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
        4  C u0 p0 c0 {1,S} {2,S} {5,D}
        5  C u0 p0 c0 {3,S} {4,D} {13,S}
        6  H u0 p0 c0 {1,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {2,S}
        9  H u0 p0 c0 {2,S}
        10 H u0 p0 c0 {3,S}
        11 H u0 p0 c0 {3,S}
        12 H u0 p0 c0 {3,S}
        13 H u0 p0 c0 {5,S}
        """),
)
            
species(
    label='S(7422)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
        2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
        3  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
        4  C u0 p0 c0 {1,S} {2,S} {6,D}
        5  C u1 p0 c0 {3,S} {6,S} {16,S}
        6  C u0 p0 c0 {4,D} {5,S} {17,S}
        7  H u0 p0 c0 {1,S}
        8  H u0 p0 c0 {1,S}
        9  H u0 p0 c0 {1,S}
        10 H u0 p0 c0 {2,S}
        11 H u0 p0 c0 {2,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {3,S}
        15 H u0 p0 c0 {3,S}
        16 H u0 p0 c0 {5,S}
        17 H u0 p0 c0 {6,S}
        """),
)
            
species(
    label='S(1145022)',
    reactive=True,
    structure=adjacencyList(
        """
        1  C u0 p0 c0 {8,S} {14,S} {15,S} {22,S}
        2  C u0 p0 c0 {10,S} {16,S} {17,S} {18,S}
        3  C u0 p0 c0 {9,S} {19,S} {20,S} {21,S}
        4  C u1 p0 c0 {5,S} {6,S} {7,S}
        5  C u0 p0 c0 {4,S} {11,S} {23,D}
        6  C u0 p0 c0 {4,S} {12,S} {24,D}
        7  C u0 p0 c0 {4,S} {13,S} {25,D}
        8  O u0 p2 c0 {1,S} {12,S}
        9  O u0 p2 c0 {3,S} {11,S}
        10 O u0 p2 c0 {2,S} {13,S}
        11 O u0 p2 c0 {5,S} {9,S}
        12 O u0 p2 c0 {6,S} {8,S}
        13 O u0 p2 c0 {7,S} {10,S}
        14 H u0 p0 c0 {1,S}
        15 H u0 p0 c0 {1,S}
        16 H u0 p0 c0 {2,S}
        17 H u0 p0 c0 {2,S}
        18 H u0 p0 c0 {2,S}
        19 H u0 p0 c0 {3,S}
        20 H u0 p0 c0 {3,S}
        21 H u0 p0 c0 {3,S}
        22 H u0 p0 c0 {1,S}
        23 O u0 p2 c0 {5,D}
        24 O u0 p2 c0 {6,D}
        25 O u0 p2 c0 {7,D}
        
        """),
)
            
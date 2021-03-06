import unittest
import ciw

class TestArrivalNode(unittest.TestCase):

    def test_init_method(self):
        ciw.seed(5)
        Q = ciw.Simulation(ciw.create_network(
            'ciw/tests/testing_parameters/params.yml'))
        N = ciw.ArrivalNode(Q)
        self.assertEqual(round(N.next_event_date, 5), 0.00440)
        self.assertEqual(N.number_of_individuals, 0)
        dates_dict = {1: {0: 0.2110410999, 1: 0.1415614623, 2: 0.3923690877},
                      2: {0: 0.1218825551, 1: 0.0044003133, 2: 0.2442775601},
                      3: {0: 0.0819463473, 1: 0.4135097542, 2: 0.7256307839},
                      4: {0: 0.1738823223, 1: 0.3988184145, 2: 0.2987813628}}
        self.assertEqual({nd: {obs: round(N.event_dates_dict[nd][obs], 10)
            for obs in N.event_dates_dict[nd]} for nd in N.event_dates_dict},
            dates_dict)

    def test_initialise_event_dates_dict_method(self):
        ciw.seed(6)
        Q = ciw.Simulation(ciw.create_network(
            'ciw/tests/testing_parameters/params.yml'))
        N = ciw.ArrivalNode(Q)
        dates_dict_1 = {1: {0: 0.4362282541, 1: 0.2672232406, 2: 0.3864256273},
                        2: {0: 0.1636952311, 1: 0.0714709565, 2: 0.8065738414},
                        3: {0: 0.4088480190, 1: 0.0514323248, 2: 0.8132038176},
                        4: {0: 1.1573751438, 1: 0.4649276714, 2: 0.8176876727}}
        dates_dict_2 = {1: {0: 0.0325870775, 1: 0.8054262558, 2: 0.8168179515},
                        2: {0: 0.0841671381, 1: 0.0328245299, 2: 0.2196023847},
                        3: {0: 0.2519089068, 1: 0.0573597814, 2: 1.5117882121},
                        4: {0: 0.8881158889, 1: 0.0560592622, 2: 2.1307650868}}
        self.assertEqual({nd: {obs: round(N.event_dates_dict[nd][obs], 10)
            for obs in N.event_dates_dict[nd]} for nd in N.event_dates_dict},
            dates_dict_1)
        N.initialise_event_dates_dict()
        self.assertEqual({nd: {obs: round(N.event_dates_dict[nd][obs], 10)
            for obs in N.event_dates_dict[nd]} for nd in N.event_dates_dict},
            dates_dict_2)

    def test_repr_method(self):
        Q = ciw.Simulation(ciw.create_network(
            'ciw/tests/testing_parameters/params.yml'))
        N = ciw.ArrivalNode(Q)
        self.assertEqual(str(N), 'Arrival Node')

    def test_find_next_event_date_method(self):
        ciw.seed(1)
        Q = ciw.Simulation(ciw.create_network(
            'ciw/tests/testing_parameters/params.yml'))
        N = ciw.ArrivalNode(Q)
        self.assertEqual(round(N.next_event_date, 5), 0.00105)
        N.find_next_event_date()
        self.assertEqual(round(N.next_event_date, 5), 0.00105)
        self.assertEqual(N.next_node, 1)
        self.assertEqual(N.next_class, 1)

        N.have_event()
        self.assertEqual(round(N.next_event_date, 5), 0.00518)
        self.assertEqual(N.next_node, 3)
        self.assertEqual(N.next_class, 1)

    def test_have_event_method(self):
        ciw.seed(1)
        Q = ciw.Simulation(ciw.create_network(
            'ciw/tests/testing_parameters/params.yml'))
        N = ciw.ArrivalNode(Q)
        self.assertEqual(Q.transitive_nodes[0].all_individuals, [])
        self.assertEqual(Q.transitive_nodes[0].individuals, [[]])
        self.assertEqual(Q.transitive_nodes[1].all_individuals, [])
        self.assertEqual(Q.transitive_nodes[1].individuals, [[]])
        self.assertEqual(Q.transitive_nodes[2].all_individuals, [])
        self.assertEqual(Q.transitive_nodes[2].individuals, [[]])
        self.assertEqual(Q.transitive_nodes[3].all_individuals, [])
        self.assertEqual(Q.transitive_nodes[3].individuals, [[]])
        self.assertEqual(round(N.next_event_date, 5), 0.00105)
        self.assertEqual(N.next_node, 1)

        N.have_event()
        self.assertEqual([str(obj) for obj in Q.transitive_nodes[0].all_individuals], ['Individual 1'])
        self.assertEqual([str(obj) for pr_cls in Q.transitive_nodes[0].individuals  for obj in pr_cls], ['Individual 1'])
        self.assertEqual(Q.transitive_nodes[1].all_individuals, [])
        self.assertEqual(Q.transitive_nodes[1].individuals, [[]])
        self.assertEqual(Q.transitive_nodes[2].all_individuals, [])
        self.assertEqual(Q.transitive_nodes[2].individuals, [[]])
        self.assertEqual(Q.transitive_nodes[3].all_individuals, [])
        self.assertEqual(Q.transitive_nodes[3].individuals, [[]])
        self.assertEqual(round(N.next_event_date, 5), 0.00518)
        self.assertEqual(N.next_node, 3)

        ciw.seed(12)
        Q = ciw.Simulation(ciw.create_network(
            'ciw/tests/testing_parameters/params.yml'))
        N = ciw.ArrivalNode(Q)
        self.assertEqual(Q.transitive_nodes[0].all_individuals, [])
        self.assertEqual(Q.transitive_nodes[0].individuals, [[]])
        self.assertEqual(Q.transitive_nodes[1].all_individuals, [])
        self.assertEqual(Q.transitive_nodes[1].individuals, [[]])
        self.assertEqual(Q.transitive_nodes[2].all_individuals, [])
        self.assertEqual(Q.transitive_nodes[2].individuals, [[]])
        self.assertEqual(Q.transitive_nodes[3].all_individuals, [])
        self.assertEqual(Q.transitive_nodes[3].individuals, [[]])
        self.assertEqual(round(N.next_event_date, 5), 0.01938)
        self.assertEqual(N.next_node, 3)

        N.have_event()
        self.assertEqual(Q.transitive_nodes[0].all_individuals, [])
        self.assertEqual(Q.transitive_nodes[0].individuals, [[]])
        self.assertEqual(Q.transitive_nodes[1].all_individuals, [])
        self.assertEqual(Q.transitive_nodes[1].individuals, [[]])
        self.assertEqual([str(obj) for obj in Q.transitive_nodes[2].all_individuals], ['Individual 1'])
        self.assertEqual([str(obj) for pr_cls in Q.transitive_nodes[2].individuals  for obj in pr_cls], ['Individual 1'])
        self.assertEqual(Q.transitive_nodes[3].all_individuals, [])
        self.assertEqual(Q.transitive_nodes[3].individuals, [[]])
        self.assertEqual(round(N.next_event_date, 5), 0.02021)
        self.assertEqual(N.next_node, 2)

    def test_no_arrivals_example(self):
        params = ciw.load_parameters(
            'ciw/tests/testing_parameters/params.yml')
        params['Arrival_distributions']['Class 0'] = ['NoArrivals',
                                                     ['Exponential', 1.0],
                                                     ['Exponential', 4.0],
                                                     ['Exponential', 3.5]]
        Q = ciw.Simulation(ciw.create_network(params))
        AN = Q.nodes[0]
        self.assertEqual(AN.simulation.network.customer_classes[0].arrival_distributions[0], 'NoArrivals')
        self.assertEqual(AN.inter_arrival(1, 0, 0.0), float('Inf'))

    def test_rejection_dict(self):
        params = {'Arrival_distributions':[['Deterministic', 3.0], ['Deterministic', 4.0]],
                  'Service_distributions':[['Deterministic', 10.0], ['Deterministic', 10.0]],
                  'Transition_matrices':[[0.0, 1.0], [0.0, 0.0]],
                  'Number_of_servers':[1, 1],
                  'Queue_capacities':[1, 1]}
        Q = ciw.Simulation(ciw.create_network(params))
        self.assertEqual(Q.rejection_dict, {1: {0: []}, 2: {0:[]}})
        Q.simulate_until_max_time(20)
        self.assertEqual(Q.rejection_dict, {1: {0: [9.0, 12.0, 18.0]}, 2: {0: [12.0, 16.0]}})

    def test_send_individual(self):
        params = {'Arrival_distributions':[['Exponential', 3.0]],
                  'Service_distributions':[['Exponential', 10.0]],
                  'Transition_matrices':[[0.5]],
                  'Number_of_servers':[1]}
        Q = ciw.Simulation(ciw.create_network(params))
        AN = Q.nodes[0]
        ind1 = ciw.Individual(555)
        ind2 = ciw.Individual(666)
        self.assertEqual(Q.nodes[1].all_individuals, [])
        self.assertEqual(Q.nodes[1].individuals, [[]])
        AN.send_individual(Q.nodes[1], ind1)
        self.assertEqual(Q.nodes[1].all_individuals, [ind1])
        self.assertEqual(Q.nodes[1].individuals, [[ind1]])
        AN.send_individual(Q.nodes[1], ind2)
        self.assertEqual(Q.nodes[1].all_individuals, [ind1, ind2])
        self.assertEqual(Q.nodes[1].individuals, [[ind1, ind2]])

    def test_report_rejection(self):
        params = {'Arrival_distributions':[['Exponential', 3.0]],
                  'Service_distributions':[['Exponential', 10.0]],
                  'Transition_matrices':[[0.5]],
                  'Number_of_servers':[1]}
        Q = ciw.Simulation(ciw.create_network(params))
        AN = Q.nodes[0]
        AN.next_event_date = 3.33
        self.assertEqual(AN.rejection_dict, {1: {0: []}})
        AN.record_rejection(Q.nodes[1])
        self.assertEqual(AN.rejection_dict, {1: {0: [3.33]}})
        AN.next_event_date = 4.44
        AN.record_rejection(Q.nodes[1])
        self.assertEqual(AN.rejection_dict, {1: {0: [3.33, 4.44]}})




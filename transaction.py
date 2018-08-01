#encapsulats our current json implementation for a transaction
class Transaction:

    #copies create transaction client method
    def __init__(self,inputs, n_output_groups, v_output_groups, output_group, timeout):
        self.inputs = inputs
        self.n_output_groups = n_output_groups
        self.v_output_groups = v_output_groups
        self.output_group = output_group
        self.timeout = timeout
        pass

    # we should stop using json dumps because it's more like json dumbs
    def serialize(self):
        return json.dumps({'inputs': inputs, 'n': n_output_groups, 'v': v_output_groups, 'outputs': output_group, 'timeout': timeout})
    pass
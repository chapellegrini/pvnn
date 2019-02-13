# keras_layers.py
# This file contains a dictionnary of hardcoded layers
# that will be used to generate Javascript code

# Built-in activation functions - see keras/activations.py
# some of them can take additional options
keras_activations = {
  'softmax': {},
  'elu': {},
  'selu': {},
  'softplus': {},
  'softsign': {},
  'relu': {},
  'tanh': {},
  'sigmoid': {},
  'hard_sigmoid': {},
  'linear': {}
}

# Built-in initializers - see keras/initializers.py
# some of them can take additional options
keras_initializers = {
  'Initializer': {},
  'Zeros': {},
  'Ones': {},
  'Constant': {},
  'RandomNormal': {},
  'RandomUniform': {},
  'TruncatedNormal': {},
  'VarianceScaling': {},
  'Orthogonal': {},
  'Identity': {},
  'lecun_uniform': {},
  'glorot_normal': {},
  'glorot_uniform': {},
  'he_normal': {},
  'lecun_normal': {},
  'he_uniform': {}
}

# Available penalties - see keras/regularizers.py
# some of them can take additional options
keras_regularizers = {
  'l1': {},
  'l2': {},
  'l1_l2': {}
}

# Built-in constraints - see keras/constraints.py
# some of them can take additional options
keras_constraints = {
  'max_norm': {},
  'non_neg': {},
  'unit_norm': {},
  'min_max_norm': {}
}

# Contains the list of keras core layers to be used by the code generating function below
# List based off https://keras.io/layers/about-keras-layers/
keras_core_layers = {
  'Dense': {
    'units': {
      'type': 'int',
      'conditions': ['>0']
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
    },
    'use_bias': {
      'type': 'boolean'
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'activity_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    }
  },

  'Activation': {
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
     }
  },

  'Dropout': {
    'rate': {
      'type': 'float',
      'conditions': ['>=0'] + ['<=1']
    },
    'noise_shape': {
      'type': 'list',
      'list': ['None']
      #:TODO:LUC:05/04/2018:To complete (1D int tensor)
    },
    'seed': {
      'type': 'int'
    }
  },

  'Flatten': {

  },

  'Input': {
    'shape': {
      'type': 'tuple_int'
    },
    'batch_shape': {
      'type': 'tuple_int'
    },
    'name': {
      'type': 'string'
    },
    'dtype': {
      'type': 'string'
    },
    'sparse': {
      'type': 'boolean'
    },
    #'tensor': {
      #:TODO:LUC:05/04/2018:To complete (Optional existing tensor)
    #}
  },

  'Reshape': {
    'target_shape': {
      'type': 'tuple_int'
    }
  },

  'Permute': {
    'dims': {
      'type': 'tuple_int',
      'conditions': ['>=1']
    }
  },

  'RepeatVector': {
    'n': {
      'type': 'int'
    }
  },

  'Lambda': {
    'function': {
      'type': 'function'
    }
    #'output_shape': {}, #only relevant when using Theano
    #'arguments': {}, #optional, not yet implemented
  },

  'ActivityRegularization': {
    'l1': {
      'type': 'float',
      'conditions': ['>=0']
    },
    'l2': {
      'type': 'float',
      'conditions': ['>=0']
    }
  },

  'Masking': {
    'mask_value': {
      'type': 'float',
      'conditions': ['>=0']
    }
  }
}

keras_convolutional_layers = {
  'Conv1D': {
    'filters': {
      'type': 'int'
    },
    'kernel_size': {
      'type': 'tuple_int'
    },
    'strides': {
      'type': 'tuple_int'
    },
    'padding': {
      'type': 'list',
      'list': ['valid', 'causal', 'same']
    },
    'dilation_rate': {
      'type': 'tuple_int'
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
    },
    'use_bias': {
      'type': 'boolean'
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'activity_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    }
  },

  'Conv2D': {
    'filters': {
      'type': 'int'
    },
    'kernel_size': {
      'type': 'tuple_int'
    },
    'strides': {
      'type': 'tuple_int'
    },
    'padding': {
      'type': 'list',
      'list': ['valid', 'same']
    },
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    },
    'dilation_rate': {
      'type': 'tuple_int'
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
    },
    'use_bias': {
      'type': 'boolean'
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'activity_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    }
  },

  'SeparableConv2D': {
    'filters': {
      'type': 'int'
    },
    'kernel_size': {
      'type': 'tuple_int'
    },
    'strides': {
      'type': 'tuple_int'
    },
    'padding': {
      'type': 'list',
      'list': ['valid', 'same']
    },
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    },
    'depth_multiplier': {
      'type': 'int'
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
    },
    'use_bias': {
      'type': 'boolean'
    },
    'depthwise_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'pointwise_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'depthwise_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'pointwise_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'activity_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'depthwise_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'pointwise_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    }
  },

  'Conv2DTranspose': {
    'filters': {
      'type': 'int'
    },
    'kernel_size': {
      'type': 'tuple_int'
    },
    'strides': {
      'type': 'tuple_int'
    },
    'padding': {
      'type': 'list',
      'list': ['valid', 'same']
    },
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    },
    'dilation_rate': {
      'type': 'tuple_int'
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
    },
    'use_bias': {
      'type': 'boolean'
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'activity_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    }
  },

  'Conv3D': {
    'filters': {
      'type': 'int'
    },
    'kernel_size': {
      'type': 'tuple_int'
    },
    'strides': {
      'type': 'tuple_int'
    },
    'padding': {
      'type': 'list',
      'list': ['valid', 'same']
    },
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    },
    'dilation_rate': {
      'type': 'tuple_int'
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
    },
    'use_bias': {
      'type': 'boolean'
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'activity_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    }
  },

  'Cropping1D': {
    'cropping': {
      'type': 'tuple_int',
      'elements_number' : 2
    }
  },

  'Cropping2D': {
    'cropping': {
      'type': 'tuple_int',
      'conditions': ['<=2']
    },
   'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    }
  },

  'Cropping3D': {
    'cropping': {
      'type': 'type_selecter',
      'dict': {
        'same for depth, height, width': {
          'type':'int'
        },
        'different symmetrical values': {
          'type': 'tuple_int',
          'elements_number' : 3
        },
        'different for all': {
          'type':'tuple_tuple_int',
          'fields': {
            'depth': {
              'type': 'tuple_int',
              'elements_number' : 2
            },
            'height': {
              'type': 'tuple_int',
              'elements_number' : 2
            },
            'width': {
              'type': 'tuple_int',
              'elements_number' : 2
            }
          }
        }
      }
    },
   'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    }
  },

  'UpSampling1D': {
    'size': {
      'type': 'int'
    }
  },

  'UpSampling2D': {
    'size': {
      'type': 'tuple_int',
      'elements_number' : 2
    },
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    }
  },

  'UpSampling3D': {
    'size': {
      'type': 'tuple_int',
      'elements_number' : 3
    },
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    }
  },

  'ZeroPadding1D': {
    'padding': {
      'type': 'tuple_int',
      'elements_number' : 2
    }
  },

  'ZeroPadding2D': {
    #'padding': {
      #:TODO:LUC:05/04/2018:To complete (int, or tuple of 2 ints, or tuple of 2 tuples of 2 ints)
    #},
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    }
  },

  'ZeroPadding3D': {
    #'padding': {
      #:TODO:LUC:05/04/2018:To complete (int, or tuple of 3 ints, or tuple of 3 tuples of 2 ints)
    #},
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    }
  }
}

keras_pooling_layers = {
  'MaxPooling1D': {
    'pool_size': {
      'type': 'int'
    },
    'strides': {
      'type': 'int' #int or none
    },
    'padding': {
      'type': 'list',
      'list': ['valid', 'same']
    }
  },

  'MaxPooling2D': {
    'pool_size': {
      'type': 'tuple_int', #int or tuple of 2 ints
      'elements_max_number' : 2
    },
    'strides': {
      'type': 'tuple_int', #int, tuple of int or none
      'elements_max_number' : 2
    },
    'padding': {
      'type': 'list',
      'list': ['valid', 'same']
    },
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    }
  },

  'MaxPooling3D': {
    'pool_size': {
      'type': 'tuple_int',
      'conditions': ['<=3']
    },
    'strides': {
      'type': 'tuple_int', #tuple of 3 ints or none
      'conditions': ['<=3']
    },
    'padding': {
      'type': 'list',
      'list': ['valid', 'same']
    },
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    }
  },

  'AveragePooling1D': {
     'pool_size': {
      'type': 'int'
    },
    'strides': {
      'type': 'int' #int or none
    },
    'padding': {
      'type': 'list',
      'list': ['valid', 'same']
    }
  },

  'AveragePooling2D': {
    'pool_size': {
      'type': 'tuple_int', #int or tuple of 2 ints
      'conditions': ['<=2']
    },
    'strides': {
      'type': 'tuple_int', #int, tuple of int or none
      'conditions': ['<=2']
    },
    'padding': {
      'type': 'list',
      'list': ['valid', 'same']
    },
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    }
  },

  'AveragePooling3D': {
    'pool_size': {
      'type': 'tuple_int',
      'conditions': ['<=3']
    },
    'strides': {
      'type': 'tuple_int', #tuple of 3 ints or none
      'conditions': ['<=3']
    },
    'padding': {
      'type': 'list',
      'list': ['valid', 'same']
    },
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    }
  },

  'GlobalMaxPooling1D': {

  },

  'GlobalAveragePooling1D': {

  },

  'GlobalMaxPooling2D': {
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    }
  },

  'GlobalAveragePooling2D': {
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    }
  }
}

keras_locally_connected_layers = {
  'LocallyConnected1D': {
    'filters': {
      'type': 'int'
    },
    'kernel_size': {
      'type': 'tuple_int'
    },
    'strides': {
      'type': 'tuple_int'
    },
    'padding': {
      'type': 'list',
      'list': ['valid']
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
    },
    'use_bias': {
      'type': 'boolean'
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'activity_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    }
  },

  'LocallyConnected2D': {
    'filters': {
      'type': 'int'
    },
    'kernel_size': {
      'type': 'tuple_int'
    },
    'strides': {
      'type': 'tuple_int'
    },
    'padding': {
      'type': 'list',
      'list': ['valid']
    },
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
    },
    'use_bias': {
      'type': 'boolean'
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'activity_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    }
  }
}

keras_recurrent_layers = {
  'rnn': {
    'cell': {
      'type': 'rnn' #TODO a coder, cf. la doc: https://keras.io/layers/recurrent/#rnn
    },
    'return_sequences': {
      'type': 'boolean'
    },
    'return_state': {
      'type': 'boolean'
    },
    'go_backwards': {
      'type': 'boolean'
    },
    'stateful': {
      'type': 'boolean'
    },
    'unroll': {
      'type': 'boolean'
    },
    'input_dim': {
      'type': 'int'
    },
    'input_length': {
      'type': 'int'
    }
  },

  'simple_rnn': {
    'units': {
      'type': 'int',
      'conditions': ['>=0']
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
     },
    'use_bias': {
      'type': 'boolean'
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'reccurent_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'reccurent_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'activity_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'reccurent_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'dropout': {
      'type': 'float',
      'conditions': ['>=0'] + ['<=1']
    },
    'reccurent_dropout': {
      'type': 'float',
      'conditions': ['>=0'] + ['<=1']
    },
    'return_sequences': {
      'type': 'boolean'
    },
    'return_state': {
      'type': 'boolean'
    },
    'go_backwards': {
      'type': 'boolean' #default: false
    },
    'stateful': {
      'type': 'boolean' #default: false
    },
    'unroll': {
      'type': 'boolean' #default: false
    }
  },

  'gru': {
    'units': {
      'type': 'int',
      'conditions': ['>=0']
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
    },
    'reccurent_activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
    },
    'use_bias': {
      'type': 'boolean'
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'reccurent_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'reccurent_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'activity_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'reccurent_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'dropout': {
      'type': 'float',
      'conditions': ['>=0'] + ['<=1']
    },
    'reccurent_dropout': {
      'type': 'float',
      'conditions': ['>=0'] + ['<=1']
    },
    'implementation': {
      'type': 'int',
      'conditions': ['>=1'] + ['<=2']
    },
    'return_sequences': {
      'type': 'boolean'
    },
    'return_state': {
      'type': 'boolean'
    },
    'go_backwards': {
      'type': 'boolean' #default: false
    },
    'stateful': {
      'type': 'boolean' #default: false
    },
    'unroll': {
      'type': 'boolean' #default: false
    },
    'reset_after': {
      'type': 'boolean'
    }
  },

  'lstm': {
    'units': {
      'type': 'int',
      'conditions': ['>=0']
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
    },
    'reccurent_activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
    },
    'use_bias': {
      'type': 'boolean'
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'reccurent_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'unit_forget_bias': {
      'type': 'boolean'
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'reccurent_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'activity_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'reccurent_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'dropout': {
      'type': 'float',
      'conditions': ['>=0', '<=1']
    },
    'reccurent_dropout': {
      'type': 'float',
      'conditions': ['>=0', '<=1']
    },
    'implementation': {
      'type': 'int',
      'conditions': ['>=1', '<=2']
    },
    'return_sequences': {
      'type': 'boolean'
    },
    'return_state': {
      'type': 'boolean'
    },
    'go_backwards': {
      'type': 'boolean' #default: false
    },
    'stateful': {
      'type': 'boolean' #default: false
    },
    'unroll': {
      'type': 'boolean' #default: false
    }
  },

  'conv_lstm_2d': {
    'filters': {
      'type': 'int'
    },
    'kernel_size': {
      'type': 'tuple_int'
    },
    'strides': {
      'type': 'tuple_int'
    },
    'padding': {
      'type': 'list',
      'list': ['valid'] + ['same']
    },
    'data_format': {
     'type': 'list',
     'list': ['channels_last', 'channels_first']
    },
    'dilation_rate': {
      'type': 'tuple_int'
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
     },
    'reccurent_activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
     },
    'use_bias': {
      'type': 'boolean'
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'reccurent_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'unit_forget_bias': {
      'type': 'boolean'
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'reccurent_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'activity_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'reccurent_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'return_sequences': {
      'type': 'boolean'
    },
    'go_backwards': {
      'type': 'boolean' #default: false
    },
    'stateful': {
      'type': 'boolean' #default: false
    },
    'dropout': {
      'type': 'float',
      'conditions': ['>=0'] + ['<=1']
    },
    'reccurent_dropout': {
      'type': 'float',
      'conditions': ['>=0'] + ['<=1']
    }
  },

  'simple_rnn_cell': {
    'units': {
      'type': 'int',
      'conditions': ['>0']
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
      #Default: hyperbolic tangent (tanh). If you pass None, no activation is applied
     },
    'use_bias': {
      'type': 'boolean'
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'reccurent_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'reccurent_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'reccurent_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'dropout': {
      'type': 'float',
      'conditions': ['>=0'] + ['<=1']
    },
    'reccurent_dropout': {
      'type': 'float',
      'conditions': ['>=0'] + ['<=1']
    }
  },

  'gru_cell': {
    'units': {
      'type': 'int',
      'conditions': ['>0']
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
      #Default: hyperbolic tangent (tanh). If you pass None, no activation is applied
     },
    'reccurent_activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
      #Default: hard sigmoid (hard_sigmoid). If you pass None, no activation is applied
     },
    'use_bias': {
      'type': 'boolean'
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'reccurent_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'reccurent_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'reccurent_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'dropout': {
      'type': 'float',
      'conditions': ['>=0', '<=1']
    },
    'reccurent_dropout': {
      'type': 'float',
      'conditions': ['>=0', '<=1']
    },
    'implementation': {
      'type': 'int',
      'conditions': ['>=1', '<=2']
    },
    'reset_after': {
      'type': 'boolean'
    }
  },

  'lstm_cell': {
    'units': {
      'type': 'int',
      'conditions': ['>0']
    },
    'activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
      #Default: hyperbolic tangent (tanh). If you pass None, no activation is applied
     },
    'reccurent_activation': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_activations]
      #Default: hard sigmoid (hard_sigmoid). If you pass None, no activation is applied
     },
    'use_bias': {
      'type': 'boolean'
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'reccurent_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'unit_forget_bias': {
      'type': 'boolean'
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'reccurent_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'reccurent_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'dropout': {
      'type': 'float',
      'conditions': ['>=0'] + ['<=1']
    },
    'reccurent_dropout': {
      'type': 'float',
      'conditions': ['>=0'] + ['<=1']
    },
    'implementation': {
      'type': 'int',
      'conditions': ['>=1'] + ['<=2']
    }
  },

  'cudnn_gru': {
    'units': {
      'type': 'int',
      'conditions': ['>0']
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'reccurent_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'reccurent_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'activity_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'reccurent_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'return_sequences': {
      'type': 'boolean'
    },
    'return_state': {
      'type': 'boolean'
    },
    'stateful': {
      'type': 'boolean'
      #Default: false
    }
  },

  'cudnn_lstm': {
    'units': {
      'type': 'int',
      'conditions': ['>0']
    },
    'kernel_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'unit_forget_bias': {
      'type': 'boolean'
    },
    'reccurent_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'bias_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'kernel_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'reccurent_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'bias_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'activity_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'kernel_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'reccurent_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'bias_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'return_sequences': {
      'type': 'boolean'
    },
    'return_state': {
      'type': 'boolean'
    },
    'stateful': {
      'type': 'boolean'
      #Default: false
    }
  }
}
keras_embedding_layers = {
  'embedding': {
    'input_dim': {
      'type': 'int',
      'conditions': ['>0']
    },
    'output_dim': {
      'type': 'int',
      'conditions': ['>=0']
    },
    'embeddings_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'embeddings_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'embeddings_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'mask_zero': {
      'type': 'boolean'
    },
    'input_length': {
      'type': 'int'
    }
  }
}

keras_merge_layers = {
  'Add': {
    #:TODO:PELLEGRINI:31/04/2018:Takes a list of tesor as input, must be the same shape
  },
  'Substract': {
    #:TODO:PELLEGRINI:31/04/2018:Takes a 2 elements list of tensor as input, must be the same shape.
    # Must include a way to order the inputs
  },
  'Multiply': {
    #:TODO:PELLEGRINI:31/04/2018:Takes a list of tesor as input, must be the same shape
  },
  'Average': {
    #:TODO:PELLEGRINI:31/04/2018:Takes a list of tesor as input, must be the same shape
  },
  'Maximum': {
    #:TODO:PELLEGRINI:31/04/2018:Takes a list of tesor as input, must be the same shape
  },
  'Concatenate': {
    'axis': {
      'type': 'int'
    }
    #:TODO:PELLEGRINI:31/04/2018:Takes a list of tesor as input, must be the same shape, except for the concatenation axis
  },
  'Dot': {
    'axes': {
      'type': 'int'
      #:TODO:LUC:05/04/2018:To complete (int or tuple of ints)
    },
    'normalize': {
      'type': 'boolean'
    }
  }
}
'''
  #:CHANGED:PELLEGRINI:31/03/2018: Commented these layers
  These layers are the functional interfaces, maybe it's useless to have the 2 versions for code generation?
  ,
  'add': {
    'inputs': {
      'type': 'list',
      #:TODO:LUC:05/04/2018:To complete (list of tensors)
    }
  },
  'substract': {
    'inputs': {
      'type': 'list',
      #:TODO:LUC:05/04/2018:To complete (list of tensors)
    }
  },
  'multiply': {
    'inputs': {
      'type': 'list',
      #:TODO:LUC:05/04/2018:To complete (list of tensors)
    }
  },
  'average': {
    'inputs': {
      'type': 'list',
      #:TODO:LUC:05/04/2018:To complete (list of tensors)
    }
  },
  'maximum': {
    'inputs': {
      'type': 'list',
      #:TODO:LUC:05/04/2018:To complete (list of tensors)
    }
  },
  'concatenate': {
    'inputs': {
      'type': 'list',
      #:TODO:LUC:05/04/2018:To complete (list of tensors)
    },
    'axis': {
      'type': 'int'
    }
  },
  'dot': {
    'inputs': {
      'type': 'list',
      #:TODO:LUC:05/04/2018:To complete (list of tensors)
    },
    'axes': {
      #:TODO:LUC:05/04/2018:To complete (int or tuple of ints)
    },
    'normalize': {
      'type': 'boolean'
    }
  }
'''

keras_advanced_activations_layers = {
  'leaky_relu': {
    'alpha': {
      'type': 'float',
      'conditions': ['>=0']
    }
  },

  'prelu': {
    'alpha_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'alpha_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'alpha_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'shared_axes': {
      'type' : 'int'
      #:TODO:LUC:05/04/2018:To complete (int or tuple of ints)
    }
  },

  'elu': {
    'alpha': {
      'type': 'float'
    }
  },

  'thresholded_relu': {
    'theta': {
      'type': 'float',
      'conditions': ['>=0']
    }
  },

  'softmax': {
     'axis': {
      'type': 'int'
    }
  }

}

keras_normalization_layers = {
  'batch_normalization': {
    'axis': {
      'type': 'int'
    },
    'momentum': {
      'type': 'float'
    },
    'epsilon': {
      'type': 'float'
    },
    'center': {
      'type': 'boolean'
    },
    'scale': {
      'type': 'boolean'
    },
    'beta_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'gamma_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'moving_mean_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'moving_variance_initializer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_initializers]
    },
    'beta_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'gamma_regularizer': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_regularizers]
    },
    'beta_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    },
    'gamma_constraint': {
      'type': 'list',
      'list': ['None'] + [s for s in keras_constraints]
    }
  }

}

keras_noise_layers = {
  'gaussian_noise': {
    'stddev': {
      'type': 'float'
    }
  },
  'gaussian_dropout': {
    'stddev': {
      'type': 'float'
    }
  },
  'alpha_dropout': {
    'stddev': {
      'type': 'float'
    },
    'seed': {
      'type': 'int'
    }
  }
}


# List of the layer categories
keras_layers_categories = {
    "Convolutional Layers" : keras_convolutional_layers,
    "Pooling Layers" : keras_pooling_layers,
    "Locally Connected Layers" : keras_locally_connected_layers,
    "Recurrent Layers" : keras_recurrent_layers,
    "Embedding Layers" : keras_embedding_layers,
    "Merge Layers" : keras_merge_layers,
    "Advanced Activation Layers" : keras_advanced_activations_layers,
    "Normalization Layers" : keras_normalization_layers,
    "Noise Layers" : keras_noise_layers
}

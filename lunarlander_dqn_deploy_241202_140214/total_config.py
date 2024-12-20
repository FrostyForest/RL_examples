exp_config = {
    'env': {
        'manager': {
            'episode_num': float("inf"),
            'max_retry': 1,
            'step_timeout': None,
            'auto_reset': True,
            'reset_timeout': None,
            'retry_type': 'reset',
            'retry_waiting_time': 0.1,
            'shared_memory': True,
            'copy_on_get': True,
            'context': 'fork',
            'wait_num': float("inf"),
            'step_wait_timeout': None,
            'connect_timeout': 60,
            'reset_inplace': False,
            'cfg_type': 'SyncSubprocessEnvManagerDict',
            'type': 'subprocess'
        },
        'stop_value': 200,
        'n_evaluator_episode': 8,
        'replay_path': None,
        'save_replay_gif': False,
        'replay_path_gif': None,
        'action_clip': False,
        'cfg_type': 'LunarLanderEnvDict',
        'type': 'lunarlander',
        'import_names': ['dizoo.box2d.lunarlander.envs.lunarlander_env'],
        'collector_env_num': 8,
        'evaluator_env_num': 8,
        'env_id': 'LunarLander-v2'
    },
    'policy': {
        'model': {
            'encoder_hidden_size_list': [512, 64],
            'obs_shape': 8,
            'action_shape': 4,
            'dueling': True
        },
        'learn': {
            'learner': {
                'train_iterations': 1000000000,
                'dataloader': {
                    'num_workers': 0
                },
                'log_policy': True,
                'hook': {
                    'load_ckpt_before_run': '',
                    'log_show_after_iter': 100,
                    'save_ckpt_after_iter': 10000,
                    'save_ckpt_after_run': True
                },
                'cfg_type': 'BaseLearnerDict'
            },
            'update_per_collect': 10,
            'batch_size': 64,
            'learning_rate': 0.001,
            'target_update_freq': 100,
            'target_theta': 0.005,
            'ignore_done': False
        },
        'collect': {
            'collector': {
                'deepcopy_obs': False,
                'transform_obs': False,
                'collect_print_freq': 100,
                'cfg_type': 'SampleSerialCollectorDict',
                'type': 'sample'
            },
            'n_sample': 64,
            'unroll_len': 1
        },
        'eval': {
            'evaluator': {
                'eval_freq': 1000,
                'render': {
                    'render_freq': -1,
                    'mode': 'train_iter'
                },
                'figure_path': None,
                'cfg_type': 'InteractionSerialEvaluatorDict',
                'stop_value': 200,
                'n_episode': 8
            }
        },
        'other': {
            'replay_buffer': {
                'type': 'advanced',
                'replay_buffer_size': 100000,
                'max_use': float("inf"),
                'max_staleness': float("inf"),
                'alpha': 0.6,
                'beta': 0.4,
                'anneal_step': 100000,
                'enable_track_used_data': False,
                'deepcopy': False,
                'thruput_controller': {
                    'push_sample_rate_limit': {
                        'max': float("inf"),
                        'min': 0
                    },
                    'window_seconds': 30,
                    'sample_min_limit_ratio': 1
                },
                'monitor': {
                    'sampled_data_attr': {
                        'average_range': 5,
                        'print_freq': 200
                    },
                    'periodic_thruput': {
                        'seconds': 60
                    }
                },
                'cfg_type': 'AdvancedReplayBufferDict'
            },
            'eps': {
                'type': 'exp',
                'start': 0.95,
                'end': 0.1,
                'decay': 50000
            },
            'commander': {
                'cfg_type': 'BaseSerialCommanderDict'
            }
        },
        'on_policy': False,
        'cuda': True,
        'multi_gpu': False,
        'bp_update_sync': True,
        'traj_len_inf': False,
        'type': 'dqn',
        'priority': False,
        'priority_IS_weight': False,
        'discount_factor': 0.99,
        'nstep': 3,
        'cfg_type': 'DQNPolicyDict',
        'load_path': './lunarlander_dqn_seed0/ckpt/ckpt_best.pth.tar'
    },
    'exp_name': 'lunarlander_dqn_deploy_241202_140214',
    'seed': 0
}

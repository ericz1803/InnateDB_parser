def get_custom_mapping(cls):
    mapping = {
        "subject": {
            "properties": {
                "unique_identifier": {
                    "properties": {
                        "innatedb": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        }
                    }
                },
                "alt_identifier": {
                    "properties": {
                        "ensembl": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        }
                    }
                },
                "alias": {
                    "properties": {
                        "refseq": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "uniprotkb": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "uniprotkb_name": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "hgnc_name": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                            "copy_to": ["all"],
                        },
                    }
                },
                "ncbi_taxid": {
                    "type": "integer",
                },
                "biological_role": {
                    "properties": {
                        "psi-mi": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "label": {"type": "text"},
                    }
                },
                "exp_role": {
                    "properties": {
                        "psi-mi": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "label": {"type": "text"},
                    }
                },
                "interactor_type": {
                    "properties": {
                        "psi-mi": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "label": {"type": "text"},
                    }
                },
                "participant_identification_method": {
                    "properties": {
                        "psi-mi": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "label": {"type": "text"},
                    }
                },
            }
        },
        "object": {
            "properties": {
                "unique_identifier": {
                    "properties": {
                        "innatedb": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        }
                    }
                },
                "alt_identifier": {
                    "properties": {
                        "ensembl": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        }
                    }
                },
                "alias": {
                    "properties": {
                        "refseq": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "uniprotkb": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "uniprotkb_name": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "hgnc_name": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                            "copy_to": ["all"],
                        },
                    }
                },
                "ncbi_taxid": {
                    "type": "integer",
                },
                "biological_role": {
                    "properties": {
                        "psi-mi": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "label": {"type": "text"},
                    }
                },
                "exp_role": {
                    "properties": {
                        "psi-mi": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "label": {"type": "text"},
                    }
                },
                "interactor_type": {
                    "properties": {
                        "psi-mi": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "label": {"type": "text"},
                    }
                },
                "participant_identification_method": {
                    "properties": {
                        "psi-mi": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "label": {"type": "text"},
                    }
                },
            }
        },
        "relation": {
            "properties": {
                "interaction_detection_method": {
                    "properties": {
                        "psi-mi": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "label": {"type": "text"},
                    }
                },
                "author": {"type": "text"},
                "pmid": {
                    "type": "integer",
                },
                "interaction_type": {
                    "properties": {
                        "psi-mi": {
                            "normalizer": "keyword_lowercase_normalizer",
                            "type": "keyword",
                        },
                        "label": {"type": "text"},
                    }
                },
                "source_database": {
                    "type": "keyword",
                },
                "idinteraction_in_source_db": {"type": "keyword"},
                "confidence_score": {
                    "properties": {
                        "lpr": {"type": "integer"},
                        "hpr": {"type": "integer"},
                        "np": {"type": "integer"},
                    }
                },
                "ncbi_taxid_host_organism": {
                    "type": "integer",
                },
                "creation_date": {
                    "type": "date",
                },
                "update_date": {
                    "type": "date",
                },
                "negative": {
                    "type": "text",
                },
                "expansion_method": {
                    "normalizer": "keyword_lowercase_normalizer",
                    "type": "keyword",
                },
                "annotations_interaction": {"type": "text"},
            }
        },
    }
    return mapping

# PriMeLU: Privacy focussed Meta-Learned User Preference Estimator for Cold-Start Recommendation

Privacy focussed PyTorch implementation of the paper: "MeLU: Meta-Learned User Preference Estimator for Cold-Start Recommendation", KDD, 2019.

## Usage

### Requirements

- python 3.6+
- pytorch 1.1+
- tqdm 4.32+
- pandas 0.24+

Note that, you may have a different evidence candidate list from the paper. That's because we do not open the random seeds of data generation and model training.

## Citation

If you use this code, please cite the paper.

```
@inproceedings{lee2019melu,
  title={MeLU: Meta-Learned User Preference Estimator for Cold-Start Recommendation},
  author={Lee, Hoyeop and Im, Jinbae and Jang, Seongwon and Cho, Hyunsouk and Chung, Sehee},
  booktitle={Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery \& Data Mining},
  pages={1073--1082},
  year={2019},
  organization={ACM}
}
```

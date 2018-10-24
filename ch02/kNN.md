
# k-近邻算法的原理

### 给定分类已定的一个训练数据集，当要对新的实例进行分类时，对当前实例和训练数据集中的数据进行距离度量（用特征空间中两个实例点的距离近似反映两个实例的相似程度），按照距离大小升序排列，取前 k 个数据的分类，然后通过特定的分类决策规则作用于前 k 个数据的分类为其划分类别。k-近邻法的三个基本要素：k 值的确定、距离的度量、分类决策规则。
![knn](../resource/knn.png)

![](../resource/Lp.png)
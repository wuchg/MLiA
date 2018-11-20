### 矩阵

本质：矩阵是个数表；从线性变换的视角看，矩阵是记录线性变换这一过程的描述信息。记为 $A_{m\times n}$$  或 $$A=\{a_{ij}\}$ 或 $A=\{a_{ij}\}_{m\times n}$

#### 特殊矩阵及其性质

##### 同型矩阵

具有相同行数和列数的矩阵，称为同型矩阵。

##### 方矩阵

如果 $m$ 等于 $n$ ,称为 $n$ 阶（方）矩阵，记为 $A_{n}$。

##### 零矩阵

所有元素为零的矩阵称为零矩阵，记为 $O$ 或 $O_{m \times n}$。

##### 三角矩阵

设$A=\{a_{ij}\}_{n}$是 n 阶方阵，若：

1. $A$ 的元素满足 $a_{ij}=0$, $\forall i \gt j$ ,称 $A$ 为上三角矩阵。

2. $A$ 的元素满足 $a_{ij}=0$, $\forall i \lt j$ ,称 $A$ 为下三角矩阵。

##### 对角矩阵

元素满足$a_{ij}=0,\forall i \neq j$ ，记为 $A=diag\{a_{11},a_{22},...,a_{nn}\}=diag\{a_{ii}\}$ 。

##### 单位矩阵

对角元素为1的三角矩阵，记为$I$ 或 $I_{n}$ 。

##### 对称矩阵

设$A=\{a_{ij}\}_{n}$是 n 阶方阵，若：

1. $A$ 的元素满足 $a_{ij}=a_{ji} \quad\forall i,j \quad \Longleftrightarrow \quad A^T=A$ 
2. $A$ 的元素满足 $a_{ij}=-a_{ji} \quad\forall i,j \quad \Longleftrightarrow \quad A^T=-A$ 

#### 矩阵的基本运算及其规则

$A(B+C)=AB+AC$ 

$(B+C)A=BA+CA$

$(AB)C=A(BC)$

$\lambda(AB)=(\lambda A)B=A(\lambda B)$ ,其中 $\lambda$ 是一个数。

$AI=IA=A$

$A^{k+l}=A^{k}A^{l}$

$(A^{k})^l=A^{kl}$

$A^0=I$ （特别规定）

$(A^T)^T=A$

$(A+B)^T=A^T+B^T$

$(\lambda A)^T=\lambda A^T$,其中$\lambda 是一个数$ 。

$(AB)^T=B^TA^T$

$tr(A)=\sum_{i=1}^{n}a_{ii}=|A|=det(A)$

$tr(AB)=tr(BA)$

$|A^T|=|A|$

$|\lambda A|=\lambda^n|A|$

$|AB|=|A||B|$ 

#### 伴随矩阵

设$A=\{a_{ij}\}$ 行列式$|A|$ 的各个元素的代数余子式$A_{ij}$ 所构成的如下矩阵

$A^*=\begin{pmatrix} A_{11} & A_{21} &... &A_{n1} \\ A_{12} & A_{22} &... &A_{n2} \\\vdots & \vdots & &\vdots \\A_{1n} & A_{2n} &... &A_{nn} \end{pmatrix}$

称为矩阵$A$ 的伴随矩阵，简称伴随阵。

$AA^*=A^*A=|A|E$ 

$(kA)^*=k^{n-1}A^*$ 

#### 逆矩阵

设$A$是$n$阶矩阵，若存在矩阵$B$,使得$AB=BA=I$ ,则称矩阵$A$ 是可逆的（矩阵$B$ 是矩阵$A$ 的逆矩阵）。

1. 逆矩阵是唯一的，用$A^{-1}$ 表示。
  证明：设$B$ ,$C$ 均是$A$ 的逆矩阵，则有 $B=BI=B(AC)=(BA)C=IC=C$ 。
2. 矩阵$A$ 是可逆的的充要条件是$|A|\neq 0 $ 且 $A^{-1}=\frac{1}{|A|}A^*$ 

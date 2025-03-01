from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import Ridge
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib


def linear_model1():
    """
    线性回归：正规方程
    :return:
    """
    # 获取数据
    boston = load_boston()

    # 数据预处理
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)

    # 特征工程
    transform = StandardScaler()
    x_train = transform.fit_transform(x_train)
    x_test = transform.transform(x_test)

    # 模型训练
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)

    # 评估模型
    # score = estimator.score(x_test, y_test)
    y_pre = estimator.predict(x_test)
    # print(score)
    error = mean_squared_error(y_test, y_pre)
    print(error)


def linear_model2():
    """
    线性回归：岭回归
    :return:
    """
    # 获取数据
    boston = load_boston()

    # 数据预处理
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)

    # 特征工程
    transform = StandardScaler()
    x_train = transform.fit_transform(x_train)
    x_test = transform.transform(x_test)

    # 模型训练
    estimator = SGDRegressor(max_iter=1000)
    estimator.fit(x_train, y_train)

    # 评估模型
    # score = estimator.score(x_test, y_test)
    y_pre = estimator.predict(x_test)
    # print(score)
    error = mean_squared_error(y_test, y_pre)
    print(error)


def linear_model3():
    """
    线性回归：岭回归
    :return:
    """
    # 获取数据
    boston = load_boston()

    # 数据预处理
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)

    # 特征工程
    transform = StandardScaler()
    x_train = transform.fit_transform(x_train)
    x_test = transform.transform(x_test)

    # 模型训练
    estimator = Ridge(alpha=1)
    estimator.fit(x_train, y_train)

    # 评估模型
    # score = estimator.score(x_test, y_test)
    y_pre = estimator.predict(x_test)
    # print(score)
    error = mean_squared_error(y_test, y_pre)
    print(error)


def load_dump_demo():
    """
    线性回归：梯度下降
    :return:
    """
    # 获取数据
    boston = load_boston()

    # 数据预处理
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=22)

    # 特征工程
    transform = StandardScaler()
    x_train = transform.fit_transform(x_train)
    x_test = transform.transform(x_test)

    # 模型训练
    # estimator = Ridge(alpha=1)
    # estimator.fit(x_train, y_train)

    # 模型保存
    # joblib.dump(estimator, '../data/test.pkl')

    # 模型加载
    estimator = joblib.load('../data/test.pkl')

    # 评估模型
    # score = estimator.score(x_test, y_test)
    y_pre = estimator.predict(x_test)
    # print(score)
    error = mean_squared_error(y_test, y_pre)
    print(error)


if __name__ == '__main__':
    # linear_model1()
    # linear_model2()
    # linear_model3()
    load_dump_demo()

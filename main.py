import matplotlib.pyplot as plt
import sympy
import numpy as np

def calculate_points(delta_x, delta_y, x0, y0, depth, step) -> tuple[list, list]:
    points_x = []
    points_y = []

    try:
        for _ in range(depth):
            x0 = x0 - step * delta_x.subs({'x': x0, 'y': y0})
            y0 = y0 - step * delta_y.subs({'x': x0, 'y': y0})
            points_x.append(float(x0))
            points_y.append(float(y0))

    except:
        print("Um erro ocorreu na execução do seu programa.")
        print("Verifique se o seu sistema possui solução.")
        exit(1)

    return points_x, points_y


def plot_function(f, plot_points_x, plot_points_y, axis_size) -> None:
    f_lambdified = sympy.lambdify(('x', 'y'), f, 'numpy')

    x_values = np.linspace(-axis_size, axis_size, 100)
    y_values = np.linspace(-axis_size, axis_size, 100)
    X, Y = np.meshgrid(x_values, y_values)
    Z = f_lambdified(X, Y)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    
    Z_points = [f_lambdified(plot_points_x[i], plot_points_y[i]) for i in range(len(plot_points_x))]
    ax.scatter(plot_points_x, plot_points_y, Z_points, color='red')
    
    ax.set_xlim([-axis_size, axis_size])
    ax.set_ylim([-axis_size, axis_size])
    ax.set_zlim([Z.min(), Z.max()])

    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')

    plt.show()

def main():
    f = sympy.sympify(input("f(x, y) = "))
    x0, y0 = tuple(map(float, input("Chute inicial no formato a,b: ").strip().split(",")))
    axis_size = int(input("Tamanho do eixo: "))

    f_line_x = sympy.diff(f, "x")
    f_line_y = sympy.diff(f, "y")

    delta_x, delta_y = f_line_x, f_line_y

    depth = int(input("Depth: "))
    step = float(input("Step: "))

    plot_points_x, plot_points_y = calculate_points(delta_x, delta_y, x0, y0, depth, step)
    plot_points_x.insert(0, x0)
    plot_points_y.insert(0, y0)

    plot_function(f, plot_points_x, plot_points_y, axis_size)
    plt.show()

if __name__ == "__main__":
    main()
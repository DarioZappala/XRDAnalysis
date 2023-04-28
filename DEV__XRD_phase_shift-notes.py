

    def get_theta(self):
        """Tabulated peaks of both phases."""
        # Merge peaks of the two phases
        theta = []
        intensity = []
        position = []
        for idx in [0, 1]:
            t, i, p = self.get_theta_partial(idx)
            theta += [t]
            intensity += [i]
            position += [p]
        theta = concatenate(theta)
        intensity = concatenate(intensity)
        position = concatenate(position)

        # Sort peaks by increasing theta
        idx_sorted = argsort(theta)
        theta, intensity = theta[idx_sorted], intensity[idx_sorted]

        # Assign position to peaks based on decreasing intensity
        position = empty(len(theta), dtype = int)
        idx_sorted = argsort(intensity)[::-1]
        position[idx_sorted] = range(len(theta))

        return theta, intensity, position
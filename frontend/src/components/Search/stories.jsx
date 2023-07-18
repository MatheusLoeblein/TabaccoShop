import { Search } from '.';

export default {
    title: 'Search',
    component: Search,
    args: {
        children: 'Search',
    }
};

export const Template = (args) => {
    return (
        <div>
            <Search {...args} />
        </div>
    );
};

import { Header } from '.';

export default {
    title: 'Header',
    component: Header,
    args: {
        children: 'TabaccoShop',
    },
    argTypes: {
        children: { type: 'string' },
    },
};

export const Template = (args) => {
    return (
        <div>
            <Header {...args} />
        </div>
    );
};

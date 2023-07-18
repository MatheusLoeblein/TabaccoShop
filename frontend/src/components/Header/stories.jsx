import { Header } from '.';

export default {
    title: 'Header',
    component: Header,
};

export const Template = (args) => {
    return (
        <div>
            <Header {...args} />
        </div>
    );
};

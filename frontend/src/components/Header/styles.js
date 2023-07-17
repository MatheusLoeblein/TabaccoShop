import styled, { css } from 'styled-components';

export const Container = styled.div`
    ${({ theme }) => css`
        background: ${theme.colors.primaryColor};
        display: flex;
        color: white;
    `}
`;

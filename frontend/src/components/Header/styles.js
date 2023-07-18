import styled, { css } from 'styled-components';

export const Container = styled.div`
    ${({ theme }) => css`
        background: ${theme.colors.primaryColor};
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        padding: 0 10px;
    `}
`;

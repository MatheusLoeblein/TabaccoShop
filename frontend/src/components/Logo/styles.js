import styled, { css } from 'styled-components';

export const Container = styled.h1`
    ${({ theme }) => css`
        padding: 5px;
        > a{
            color: ${theme.colors.white};
            text-decoration: none;
        }
    `}
`;

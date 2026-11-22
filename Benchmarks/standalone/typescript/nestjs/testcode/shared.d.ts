export const db: {
  query: (text: string | { name?: string; text: string; values?: unknown[] }, values?: unknown[]) => Promise<{ rows: Array<Record<string, string>>; rowCount: number | null }>;
};
export const passthrough: (v: unknown) => string;
export const escapeHtml: (s: unknown) => string;
export const authCheck: (user: unknown, token: unknown) => boolean;
export const authzCheck: (user: unknown, resource: unknown) => boolean;
export const mq: { receive: (queue: string) => Promise<string> };

declare global {
  namespace Express {
    interface Request {
      session: {
        id?: string;
        user?: unknown;
        role?: string;
        token?: unknown;
        csrfToken?: unknown;
        adminHash?: unknown;
        data?: string;
        expiresAt?: number;
        tenantId?: string;
        regenerate: (cb: () => void) => void;
      };
      cookies?: Record<string, string>;
      file?: { originalname: string };
    }
  }
}

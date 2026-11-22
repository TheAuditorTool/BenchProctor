declare module "*";
declare namespace Express { interface Request {} }
declare module "express" {
  export interface Request extends Express.Request {
    query: Record<string, string | string[]>;
    body: any;
    params: Record<string, string>;
    headers: Record<string, string | string[] | undefined>;
    method: string;
    path: string;
    url: string;
    originalUrl: string;
    app: { locals: Record<string, unknown> };
    get(name: string): string | undefined;
  }
  export interface Response {
    status(code: number): Response;
    json(body: any): Response;
    send(body: any): Response;
    cookie(name: string, value: any, opts?: any): Response;
    redirect(url: string): void;
    redirect(status: number, url: string): void;
    location(url: string): Response;
    sendStatus(code: number): Response;
    set(field: string, value: any): Response;
    append(field: string, value: string | string[]): Response;
    setHeader(name: string, value: any): void;
    type(t: string): Response;
    end(chunk?: string): void;
  }
  export type NextFunction = any;
  export const Router: any;
  interface Express {
    (): any;
    json(options?: any): any;
    urlencoded(options?: any): any;
    text(options?: any): any;
    static(root: string, options?: any): any;
  }
  const express: Express;
  export default express;
}
declare module "fastify" {
  export type FastifyRequest = any;
  export type FastifyReply = any;
  export type FastifyInstance = any;
  const Fastify: (options?: any) => any;
  export default Fastify;
}
declare module "hono" {
  export type Context = any;
  export type Next = any;
  export const Hono: any;
}
declare module "hono/cookie" {
  export const getCookie: any;
  export const setCookie: any;
}
declare module "react" {
  export type ReactNode = any;
  export type FC<P = any> = (props: P) => any;
  export function useState<S>(
    initial: S | (() => S)
  ): [S, (value: S | ((prev: S) => S)) => void];
  export const useEffect: any;
  export const useMemo: any;
  export const useCallback: any;
  export const useRef: any;
  const React: any;
  export default React;
}
declare module "next/server" {
  export const NextResponse: any;
}
declare module "next/headers" {
  export const cookies: any;
  export const headers: any;
}
declare module "@sveltejs/kit" {
  export type RequestHandler = (event: RequestEvent) => Response | Promise<Response>;
  export function json(data: any, init?: any): Response;
}
interface RequestEvent {
  url: URL;
  request: Request;
  cookies: { get(name: string): string | undefined; set(name: string, value: string, opts?: any): void };
  params: Record<string, string>;
}
declare module "@prisma/client" { export const PrismaClient: any; }
declare module "@prisma/adapter-pg" { export const PrismaPg: any; }
declare module "sequelize" { export const Sequelize: any; export const DataTypes: any; }
declare module "typeorm" { export const DataSource: any; }
declare module "knex" { const knex: any; export default knex; }
declare module "drizzle-orm" { export const sql: any; }
declare module "drizzle-orm/better-sqlite3" { export const drizzle: any; }
declare module "better-sqlite3" { const Database: any; export default Database; }
declare module "mongodb" { export const MongoClient: any; }
declare module "mongoose" { const mongoose: any; export default mongoose; }
declare module "ajv" { const Ajv: any; export default Ajv; }
declare module "yup" { export const string: any; }
declare module "express-validator" { export const body: any; export const validationResult: any; }
declare module "redis" { export const createClient: any; }
declare module "ioredis" { export const Redis: any; }
declare module "pg" { export const Pool: any; export const escapeIdentifier: any; }
declare module "axios" { const axios: any; export default axios; }
declare module "lodash" { const lodash: any; export default lodash; }
declare module "libxmljs2" { export function parseXmlString(source: string, options?: Record<string, boolean | string | undefined>): unknown; }
declare module "cookie" {
  export interface SetCookie {
    name: string; value?: string; domain?: string; expires?: Date; httpOnly?: boolean; maxAge?: number;
    partitioned?: boolean; path?: string; priority?: "low" | "medium" | "high"; sameSite?: boolean | "lax" | "strict" | "none"; secure?: boolean;
  }
  export function stringifySetCookie(cookie: SetCookie, options?: { encode?(value: string): string }): string;
  export function parseCookie(header: string, options?: { decode?(value: string): string }): Record<string, string | undefined>;
}
declare module "@aws-sdk/client-s3" {
  export const S3Client: any;
  export const GetObjectCommand: any;
  export const PutObjectCommand: any;
}
declare module "@aws-sdk/client-iam" {
  export const IAMClient: any;
  export const PutRolePolicyCommand: any;
}
declare module "@aws-sdk/client-sts" {
  export const STSClient: any;
  export const AssumeRoleCommand: any;
}
declare module "@aws-sdk/client-sqs" {
  export const SQSClient: any;
  export const SendMessageCommand: any;
}
declare module "@aws-sdk/client-ssm" {
  export const SSMClient: any;
  export const GetParameterCommand: any;
}
declare module "ldapjs" {
  export interface SearchCallbackResponse {
    on(event: "searchEntry" | "searchReference" | "error" | "end", listener: (...args: unknown[]) => void): SearchCallbackResponse;
  }
  export interface Client {
    on(event: string, listener: (...args: unknown[]) => void): Client;
    search(base: string, options: { filter?: string; scope?: "base" | "one" | "sub"; attributes?: string[] }, callback: (error: Error | null, res: SearchCallbackResponse) => void): void;
    bind(dn: string, password: string, callback: (error: Error | null) => void): void;
    compare(dn: string, attribute: string, value: string, callback: (error: Error | null, matched?: boolean) => void): void;
    modify(dn: string, change: { operation: "add" | "delete" | "replace"; modification: Record<string, string | string[]> }, callback: (error: Error | null) => void): void;
    unbind(callback?: (error?: Error) => void): void;
  }
  export function createClient(options: { url: string | string[] }): Client;
}
declare module "libxmljs" {
  export interface XMLParseOptions {
    noent?: boolean; dtdload?: boolean; nonet?: boolean; huge?: boolean;
    [flag: string]: boolean | undefined;
  }
  export interface Document { validate(schema: Document): boolean; }
  export function parseXml(source: string, options?: XMLParseOptions): Document;
  export function parseXmlAsync(source: string, options?: XMLParseOptions): Promise<Document>;
}
declare var process: any;
declare var Buffer: any;
interface Buffer { length: number; toString(encoding?: string): string; }
declare var global: any;
declare var module: any;
declare var __dirname: string;
declare var __filename: string;
declare var console: any;
declare function require(moduleName: string): any;
declare function setImmediate(cb: (...args: any[]) => void, ...args: any[]): any;
declare function setTimeout(cb: (...args: any[]) => void, ms?: number, ...args: any[]): any;
declare function clearTimeout(id: any): void;
declare function setInterval(cb: (...args: any[]) => void, ms?: number, ...args: any[]): any;
declare function clearInterval(id: any): void;
declare function fetch(input: any, init?: any): Promise<any>;
declare class URL {
  constructor(input: string, base?: string);
  hostname: string; href: string; pathname: string; protocol: string;
  username: string; password: string;
  searchParams: { get(name: string): string | null; getAll(name: string): string[] };
}
declare class Headers { constructor(init?: any); get(name: string): string | null; set(name: string, value: string): void; }
declare class Request {
  constructor(input: any, init?: any);
  url: string; method: string; headers: Headers;
  json(): Promise<any>; text(): Promise<string>; formData(): Promise<any>;
}
declare class Response {
  constructor(body?: any, init?: any);
  static json(data: any, init?: any): Response;
  status: number; headers: Headers;
}
declare class File { name: string; size: number; type: string; }
declare namespace Express {
  namespace Multer {
    interface File { originalname: string; buffer: any; mimetype: string; size: number; }
  }
}
type ExecutionContext = any;
declare module "@nestjs/common" {
  export type ExecutionContext = any;
  export type ArgumentsHost = any;
  export interface CanActivate {
    canActivate(context: ExecutionContext): boolean | Promise<boolean>;
  }
  export interface ExceptionFilter {
    catch(exception: unknown, host: ArgumentsHost): void;
  }
  export const Body: any;
  export const Catch: any;
  export const Controller: any;
  export const Get: any;
  export const Header: any;
  export const Headers: any;
  export const Injectable: any;
  export const Module: any;
  export const Param: any;
  export const Post: any;
  export const Query: any;
  export const Redirect: any;
  export const Req: any;
  export const Res: any;
  export const StreamableFile: any;
  export const UploadedFile: any;
  export const UseFilters: any;
  export const UseGuards: any;
  export const UseInterceptors: any;
  export const UsePipes: any;
  export const ValidationPipe: any;
  export const createParamDecorator: any;
  export const BadRequestException: any;
  export const ForbiddenException: any;
  export class HttpException {
    constructor(response: string | Record<string, unknown>, status: number);
    getStatus(): number;
    getResponse(): string | object;
  }
  export const InternalServerErrorException: any;
  export const NotFoundException: any;
  export const UnauthorizedException: any;
}
declare module "http" {
  export interface IncomingMessage {
    method?: string;
    url?: string;
    headers: Record<string, string | string[] | undefined>;
    on(event: string, listener: (...args: any[]) => void): this;
  }
  export interface ServerResponse {
    writeHead(status: number, headers?: Record<string, string>): this;
    end(data?: string): void;
  }
  export interface Server { listen(port: number, host?: string): this; }
  export interface ClientRequest { on(event: string, listener: (...args: any[]) => void): this; }
  export function createServer(handler: (req: IncomingMessage, res: ServerResponse) => void): Server;
  export function get(url: string, callback?: (res: IncomingMessage) => void): ClientRequest;
}
declare var _loginAttempts: Record<string, number>;
declare var lastRequestValue: any;
declare var _stateLock: Promise<any>;
declare var sharedState: any;
declare namespace JSX {
  type Element = any;
  interface IntrinsicElements { [name: string]: any; }
}
declare module "react/jsx-runtime" {
  export const jsx: any;
  export const jsxs: any;
  export const Fragment: any;
}
declare module "react/jsx-dev-runtime" {
  export const jsxDEV: any;
  export const Fragment: any;
}
declare module "react" {
  export function useState<T>(initial: T): [T, (next: T) => void];
  export function useEffect(effect: () => void | (() => void), deps?: readonly any[]): void;
}
declare module "vue" {
  export function ref<T>(value: T): { value: T };
  export function computed<T>(getter: () => T): T;
  export function watch<T>(source: T, cb: (value: any, previous?: any) => void): void;
  export function onMounted(cb: () => void): void;
  export function onUnmounted(cb: () => void): void;
  export function createApp(
    component: any, props?: Record<string, unknown>
  ): { mount(target: any): unknown };
}
declare module "svelte" {
  export function onMount(cb: () => void | (() => void)): void;
  export function mount(
    component: any, options: { target: any; props?: Record<string, unknown> }
  ): unknown;
}
declare function $state<T>(initial: T): T;
declare function $props<T = any>(): T;
declare function $derived<T>(expr: T): T;
declare function $effect(fn: () => void | (() => void)): void;
declare namespace $derived {
  function by<T>(fn: () => T): T;
}
declare module "@angular/core" {
  export const Component: any;
  export const HostListener: any;
  export const Input: any;
  export const inject: any;
  export const signal: any;
  export const effect: any;
}
declare module "@angular/platform-browser" {
  export const DomSanitizer: any;
  export const bootstrapApplication: any;
}
declare class MessageEvent { origin: string; data: any; source: any; }
declare class URLSearchParams {
  constructor(init?: any);
  get(name: string): string | null;
  getAll(name: string): string[];
}
declare var window: {
  location: { search: string; hash: string; href: string; origin: string; pathname: string; assign(url: string): void };
  addEventListener(type: string, listener: (event: any) => void): void;
  removeEventListener(type: string, listener: (event: any) => void): void;
};
declare var document: any;
declare var localStorage: { setItem(key: string, value: string): void; getItem(key: string): string | null; removeItem(key: string): void; };
declare var sessionStorage: { setItem(key: string, value: string): void; getItem(key: string): string | null; removeItem(key: string): void; };

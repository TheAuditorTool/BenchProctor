declare module "node-serialize" {
  export function serialize(value: unknown): string;
  export function unserialize(text: string): unknown;
}

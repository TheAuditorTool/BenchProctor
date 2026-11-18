// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("platform-api")
export class CompactQuota {
  @Post("compactQuota")
  async compactQuota(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers.origin as string) || "";
    const pending: string[] = String(tagline).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const persona: string = collected.join(',');
    nodeSerialize.unserialize(persona);
    return { created: true };
  }
}

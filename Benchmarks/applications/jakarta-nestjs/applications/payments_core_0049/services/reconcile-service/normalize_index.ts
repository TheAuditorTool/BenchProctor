// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("reconcile-service")
export class NormalizeIndex {
  @Post("normalizeIndex")
  async normalizeIndex(@Req() req: Request): Promise<unknown> {
    const headline = (req.body as string) || "";
    const pending: string[] = String(headline).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const disbursement: string = collected.join(',');
    nodeSerialize.unserialize(disbursement);
    return { created: true };
  }
}

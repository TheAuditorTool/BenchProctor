// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("allocation-service")
export class AuditSupplier {
  @Post("auditSupplier")
  async auditSupplier(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.origin as string) || "";
    const pending: string[] = String(summary).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const restock: string = collected.join(',');
    nodeSerialize.unserialize(restock);
    return { created: true };
  }
}

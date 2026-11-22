// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("reconcile-service")
export class RunReconciliation {
  @Post("runReconciliation")
  async runReconciliation(@Req() req: Request): Promise<unknown> {
    const ledger = req.body.payments_payload || "";
    return new StreamableFile(Buffer.from("<section>" + ledger + "</section>"), { type: "text/html; charset=utf-8" });
  }
}

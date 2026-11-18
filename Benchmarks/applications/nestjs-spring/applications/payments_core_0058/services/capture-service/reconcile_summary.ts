// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("capture-service")
export class ReconcileSummary {
  @Post("reconcileSummary")
  async reconcileSummary(@Req() req: Request): Promise<unknown> {
    const caption = (req.body.payload as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(caption);
    const ledger: string = readInput();
    let _host = "";
    try { _host = new URL(String(ledger)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const remittance = ledger;
    http.get(remittance);
    return { created: true };
  }
}

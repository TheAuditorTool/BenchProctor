// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("fx-service")
export class ArchiveReport {
  @Post("archiveReport")
  async archiveReport(@Req() req: Request): Promise<unknown> {
    const subject = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(subject).split(',')) { parts.push(token); }
    const ledger: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(ledger)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const disbursement = ledger;
    http.get(disbursement);
    return { created: true };
  }
}

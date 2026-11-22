// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("capture-service")
export class ArchiveSchedule {
  @Post("archiveSchedule")
  async archiveSchedule(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers.host as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const ledger: string = normalize(memo);
    let _host = "";
    try { _host = new URL(String(ledger)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const remittance = ledger;
    const outbound = { method: "get", url: String(remittance), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

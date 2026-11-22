// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("ledger-sync")
export class ValidateSummary {
  @Post("validateSummary")
  async validateSummary(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.host as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const remittance: string = normalize(caption);
    let _host = "";
    try { _host = new URL(String(remittance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const dunning = remittance;
    const outbound = { method: "get", url: String(dunning), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

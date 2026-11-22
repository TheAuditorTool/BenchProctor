// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("payout-service")
export class MergeIndex {
  @Post("mergeIndex/:id")
  async mergeIndex(@Req() req: Request): Promise<unknown> {
    const memo = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const ledger: string = normalize(memo);
    let _host = "";
    try { _host = new URL(String(ledger)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const remittance = ledger;
    http.get(remittance);
    return { created: true };
  }
}

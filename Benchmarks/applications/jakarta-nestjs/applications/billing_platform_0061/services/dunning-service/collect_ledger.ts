// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("dunning-service")
export class CollectLedger {
  @Post("collectLedger/:id")
  async collectLedger(@Req() req: Request): Promise<unknown> {
    const footnote = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const remittance: string = normalize(footnote);
    let _host = "";
    try { _host = new URL(String(remittance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const arrears = remittance;
    http.get(arrears);
    return { created: true };
  }
}

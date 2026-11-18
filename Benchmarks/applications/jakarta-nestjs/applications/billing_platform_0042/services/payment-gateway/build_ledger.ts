// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("payment-gateway")
export class BuildLedger {
  @Post("buildLedger")
  async buildLedger(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.origin as string) || "";
    const _input = String(remark);
    let remittance;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': remittance = _input.normalize('NFC'); break;
      default: remittance = _input; break;
    }
    let _host = "";
    try { _host = new URL(String(remittance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const dunning = remittance;
    http.get(dunning);
    return { created: true };
  }
}

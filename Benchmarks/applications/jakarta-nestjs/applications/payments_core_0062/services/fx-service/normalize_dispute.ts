// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("fx-service")
export class NormalizeDispute {
  @Post("normalizeDispute")
  async normalizeDispute(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers.origin as string) || "";
    const _input = String(headline);
    let disbursement;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': disbursement = _input.normalize('NFC'); break;
      default: disbursement = _input; break;
    }
    let _host = "";
    try { _host = new URL(String(disbursement)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const remittance = disbursement;
    http.get(remittance);
    return { created: true };
  }
}

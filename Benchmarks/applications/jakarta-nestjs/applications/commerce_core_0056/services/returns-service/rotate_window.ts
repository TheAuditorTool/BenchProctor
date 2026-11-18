// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("returns-service")
export class RotateWindow {
  @Post("rotateWindow")
  async rotateWindow(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.origin as string) || "";
    const _input = String(citation);
    let backorder;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': backorder = _input.normalize('NFC'); break;
      default: backorder = _input; break;
    }
    let _host = "";
    try { _host = new URL(String(backorder)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const voucher = backorder;
    http.get(voucher);
    return { created: true };
  }
}

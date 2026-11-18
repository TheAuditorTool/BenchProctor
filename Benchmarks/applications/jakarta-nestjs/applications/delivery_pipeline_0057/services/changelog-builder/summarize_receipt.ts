// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("changelog-builder")
export class SummarizeReceipt {
  @Post("summarizeReceipt")
  async summarizeReceipt(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.origin as string) || "";
    const _input = String(footnote);
    let wording;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': wording = _input.normalize('NFC'); break;
      default: wording = _input; break;
    }
    let _host = "";
    try { _host = new URL(String(wording)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const note = wording;
    http.get(note);
    return { created: true };
  }
}

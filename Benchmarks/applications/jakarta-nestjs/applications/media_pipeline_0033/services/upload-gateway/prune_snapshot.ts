// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("upload-gateway")
export class PruneSnapshot {
  @Post("pruneSnapshot")
  async pruneSnapshot(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers.origin as string) || "";
    const _input = String(transcript);
    let rendition;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': rendition = _input.normalize('NFC'); break;
      default: rendition = _input; break;
    }
    let _host = "";
    try { _host = new URL(String(rendition)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const montage = rendition;
    http.get(montage);
    return { created: true };
  }
}

// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("partner-registry")
export class AnnotateDigest {
  @Post("annotateDigest")
  async annotateDigest(@Req() req: Request): Promise<unknown> {
    const blurb = (req.headers.host as string) || "";
    const handshake = `${blurb}`;
    let _host = "";
    try { _host = new URL(String(handshake)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const citation = handshake;
    http.get(citation);
    return { created: true };
  }
}

// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("manifest-builder")
export class BuildManifest {
  @Post("buildManifest")
  async buildManifest(@Req() req: Request): Promise<unknown> {
    const preface = req.body.shipping_payload || "";
    let _host = "";
    try { _host = new URL(String(preface)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const consignment = preface;
    http.get(consignment);
    return { created: true };
  }
}

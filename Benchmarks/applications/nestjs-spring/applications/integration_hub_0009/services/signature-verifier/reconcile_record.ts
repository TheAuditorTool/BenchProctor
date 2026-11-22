// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("signature-verifier")
export class ReconcileRecord {
  @Post("reconcileRecord")
  async reconcileRecord(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers.host as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const handshake: string = normalize(heading);
    let _host = "";
    try { _host = new URL(String(handshake)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const remark = handshake;
    const outbound = { method: "get", url: String(remark), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

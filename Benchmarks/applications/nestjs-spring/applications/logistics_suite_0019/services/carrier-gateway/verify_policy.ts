// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("carrier-gateway")
export class VerifyPolicy {
  @Post("verifyPolicy")
  async verifyPolicy(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.host as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const parcel: string = normalize(citation);
    let _host = "";
    try { _host = new URL(String(parcel)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const consignment = parcel;
    const outbound = { method: "get", url: String(consignment), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

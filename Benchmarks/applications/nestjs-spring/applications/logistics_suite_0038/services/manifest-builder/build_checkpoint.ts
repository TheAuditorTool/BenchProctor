// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("manifest-builder")
export class BuildCheckpoint {
  @Post("buildCheckpoint")
  async buildCheckpoint(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.host as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const consignment: string = normalize(wording);
    let _host = "";
    try { _host = new URL(String(consignment)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const parcel = consignment;
    const outbound = { method: "get", url: String(parcel), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

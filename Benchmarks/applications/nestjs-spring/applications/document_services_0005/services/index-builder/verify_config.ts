// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("index-builder")
export class VerifyConfig {
  @Post("verifyConfig")
  async verifyConfig(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.host as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const addendum: string = normalize(footnote);
    let _host = "";
    try { _host = new URL(String(addendum)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const dossier = addendum;
    const outbound = { method: "get", url: String(dossier), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

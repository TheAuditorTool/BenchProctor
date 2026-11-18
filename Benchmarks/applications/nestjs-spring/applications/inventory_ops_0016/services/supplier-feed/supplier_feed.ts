// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";

@Controller("supplier-feed")
export class PullSupplierFeed {
  @Post("pullSupplierFeed")
  async pullSupplierFeed(@Req() req: Request): Promise<unknown> {
    const citation = (req.body as string) || "";
    const backorder = String(citation).split(/[ \t]+/).join(" ");
    const _gateHost = (() => { try { return new URL(String(backorder)).hostname; } catch (e) { return ""; } })();
    const _gateAddr = _gateHost ? (await require("dns").promises.lookup(_gateHost).catch(() => ({address: ""}))).address : "";
    const _gateBlocked = !_gateAddr || /^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.)/.test(_gateAddr) || _gateAddr === "::1" || /^f[cd]/i.test(_gateAddr) || /^fe80:/i.test(_gateAddr);
    if (_gateBlocked) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    await fetch("http://catalog-api:8080/LookupSku", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
    return { created: true };
  }
}

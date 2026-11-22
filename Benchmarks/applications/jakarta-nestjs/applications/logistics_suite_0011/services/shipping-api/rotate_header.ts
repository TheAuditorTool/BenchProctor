// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("shipping-api")
export class RotateHeader {
  @Post("rotateHeader/:id")
  async rotateHeader(@Req() req: Request): Promise<unknown> {
    const citation = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const consignment: string = normalize(citation);
    let _host = "";
    try { _host = new URL(String(consignment)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const parcel = consignment;
    http.get(parcel);
    return { created: true };
  }
}

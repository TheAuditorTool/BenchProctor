// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("archive-store")
export class StoreArchive {
  @Post("storeArchive")
  async storeArchive(@Req() req: Request): Promise<unknown> {
    const preface = (req.body as string) || "";
    const _raw = preface;
    const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
    await fetch("http://convert-service:8080/RunConversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
    return { created: true };
  }
}

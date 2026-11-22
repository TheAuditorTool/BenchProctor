// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("revision-store")
export class ResolveManifest {
  @Post("resolveManifest/:id")
  async resolveManifest(@Req() req: Request): Promise<unknown> {
    const transcript = (req.params.id as string) || "";
    const _raw = transcript;
    const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
    return new StreamableFile(Buffer.from("<section>" + addendum + "</section>"), { type: "text/html; charset=utf-8" });
  }
}

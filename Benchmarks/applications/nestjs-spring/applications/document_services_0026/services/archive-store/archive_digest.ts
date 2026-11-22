// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("archive-store")
export class ArchiveDigest {
  @Post("archiveDigest")
  async archiveDigest(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.authorization as string) || "";
    const addendum = String(preface).slice(0, 200);
    const outbound = { method: "get", url: String(addendum), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}

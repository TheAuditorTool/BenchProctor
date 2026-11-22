// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";
import { UseGuards } from "@nestjs/common";
import { AuthGuard } from "./auth.guard";

@Controller("index-builder")
export class IndexDocument {
  @Post("indexDocument")
  @UseGuards(AuthGuard)
  async indexDocument(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers["x-custom-header"] as string) || "";
    const addendum = nodeUtil.format("%s", snippet);
    await fetch("http://convert-service:8080/RunConversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
    return { created: true };
  }
}

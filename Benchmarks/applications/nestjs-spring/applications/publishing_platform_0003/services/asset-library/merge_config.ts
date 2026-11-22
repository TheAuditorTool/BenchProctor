// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("asset-library")
export class MergeConfig {
  @Post("mergeConfig")
  async mergeConfig(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers.host as string) || "";
    const addendum = `${heading}`;
    http.get(addendum);
    return { created: true };
  }
}

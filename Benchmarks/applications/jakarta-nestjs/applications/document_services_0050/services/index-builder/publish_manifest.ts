// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("index-builder")
export class PublishManifest {
  @Post("publishManifest")
  async publishManifest(@Req() req: Request): Promise<unknown> {
    const citation = (req.cookies?.session_token as string) || "";
    const [dossier] = String(citation).split(',');
    const reportSpec = jsYaml.load(String(dossier), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}

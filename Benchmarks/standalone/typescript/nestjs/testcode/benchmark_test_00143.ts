// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request, Response } from "express";
import * as fs from "fs";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00143")
  async BenchmarkTest00143(@Req() req: Request): Promise<unknown> {
    const userInput = (req.body as string) || "";
    const data = String(userInput).slice(0, 200);
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(data)) { throw new ForbiddenException({error:"forbidden"}); }
    const checkedPath = "/var/app/data/" + data;
    const fileContent = fs.readFileSync(checkedPath, "utf8");
    return fileContent;
  }
}

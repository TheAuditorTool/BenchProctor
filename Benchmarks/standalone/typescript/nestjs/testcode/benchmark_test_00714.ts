// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, UploadedFile, UseInterceptors, ForbiddenException } from "@nestjs/common";
import { Response } from "express";
import * as fs from "fs";
import * as path from "path";
import { FileInterceptor } from "@nestjs/platform-express";
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
  @Post("BenchmarkTest00714")
  @UseInterceptors(FileInterceptor("file"))
  async BenchmarkTest00714(@UploadedFile() file: Express.Multer.File): Promise<unknown> {
    const userInput = file?.originalname || "";
    const _raw = userInput;
    const data = (_raw && _raw.length > 0) ? _raw : 'default';
    const resolved = path.resolve("/var/app/data", data);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const checkedPath = resolved;
    const fileContent = fs.readFileSync(checkedPath, "utf8");
    return fileContent;
  }
}

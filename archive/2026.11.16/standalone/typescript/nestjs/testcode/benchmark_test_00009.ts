// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, UploadedFile, UseInterceptors } from "@nestjs/common";
import { Request, Response } from "express";
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
  @Post("BenchmarkTest00009")
  @UseInterceptors(FileInterceptor("file"))
  async BenchmarkTest00009(@UploadedFile() file: Express.Multer.File, @Req() req: Request): Promise<unknown> {
    const userInput = file?.originalname || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const data: string = normalize(userInput);
    req.session.data = String(data);
    return { created: true };
  }
}

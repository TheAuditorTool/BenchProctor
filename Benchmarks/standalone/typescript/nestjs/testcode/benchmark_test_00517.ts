// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, UploadedFile, UseInterceptors } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00517")
  @UseInterceptors(FileInterceptor("file"))
  async BenchmarkTest00517(@UploadedFile() file: Express.Multer.File): Promise<unknown> {
    const userInput = file?.originalname || "";
    const data = String(userInput).replace(/\u0000/g, "");
    JSON.parse(data);
    return { created: true };
  }
}
